import pandas as pd
import numpy as np
from google.cloud import storage, aiplatform
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==============================================================================
# CONFIGURAÇÕES
# ==============================================================================
PROJECT_ID = "project-f38402f0-f3e4-4629-a39"
REGION = "southamerica-east1"
BUCKET_NAME = 'brazil-soccer-data'

# O Vertex AI procurará por 'model.bst' dentro desta pasta.
ARTIFACT_URI = f"gs://{BUCKET_NAME}/modelo_futebol/"
MODEL_FILE_NAME = "model.bst"

# ==============================================================================
# FUNÇÕES DE DATA E TREINAMENTO
# ==============================================================================

def load_data_from_gcs(bucket_name):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    dfs = []
    
    for blob in blobs:
        if blob.name.endswith('.csv'):
            uri = f"gs://{bucket_name}/{blob.name}"
            dfs.append(pd.read_csv(uri))
            
    df_final = pd.concat(dfs, ignore_index=True)
    df_final['date_GMT'] = pd.to_datetime(df_final['date_GMT'])
    return df_final.sort_values(by='date_GMT').reset_index(drop=True)

def preprocess_data(df):
    df = df[df['status'] == 'complete'].copy()
    
    # Cria Target: 0 (Casa), 1 (Empate), 2 (Visitante)
    conditions = [
        (df['home_team_goal_count'] > df['away_team_goal_count']),
        (df['home_team_goal_count'] == df['away_team_goal_count']),
        (df['home_team_goal_count'] < df['away_team_goal_count'])
    ]
    df['target'] = np.select(conditions, [0, 1, 2])
    
    return df

def train_and_upload(bucket_name):
    # 1. Carregamento e Preparação
    df = load_data_from_gcs(bucket_name)
    df = preprocess_data(df)
    
    # 2. Seleção de Features
    features = [
        'Pre-Match PPG (Home)', 'Pre-Match PPG (Away)',
        'home_ppg', 'away_ppg',
        'average_goals_per_match_pre_match',
        'odds_ft_home_team_win', 'odds_ft_draw', 'odds_ft_away_team_win'
    ]
    
    df_clean = df.dropna(subset=features)
    
    X = df_clean[features]
    y = df_clean['target']
    
    # 3. Divisão Treino/Teste
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # 4. Treinamento
    model = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )
    
    model.fit(X_train.values, y_train)
    
    # 5. Avaliação
    acc = accuracy_score(y_val, model.predict(X_val.values))
    print(f"Acurácia do Modelo: {acc:.2%}")
    
    # 6. Salvar e Upload para GCS
    model.save_model(MODEL_FILE_NAME)
    
    bucket = storage.Client().bucket(bucket_name)
    blob = bucket.blob(f"modelo_futebol/{MODEL_FILE_NAME}")
    blob.upload_from_filename(MODEL_FILE_NAME)
    
    return model

# ==============================================================================
# FUNÇÃO PRINCIPAL DE DEPLOY
# ==============================================================================

def deploy_to_vertex_ai():
    # 1. Registro do Modelo
    aiplatform.init(project=PROJECT_ID, location=REGION)

    model_vertex = aiplatform.Model.upload(
        display_name="futebol-previsor-restore",
        artifact_uri=ARTIFACT_URI,
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.1-7:latest"
    )
    
    # 2. Criar Endpoint e Fazer Deploy
    endpoint = model_vertex.deploy(
        machine_type="n1-standard-2",
        min_replica_count=1,
        max_replica_count=1,
        traffic_percentage=100
    )
    
    # Informações de saída para uso
    print(f"ENDPOINT_RESOURCE_NAME = \"{endpoint.resource_name}\"")
    print(f"PROJECT_ID = \"{PROJECT_ID}\"")
    print(f"REGION = \"{REGION}\"")

# ==============================================================================
# EXECUÇÃO
# ==============================================================================

if __name__ == "__main__":
    train_and_upload(BUCKET_NAME)
    deploy_to_vertex_ai()