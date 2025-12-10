import pandas as pd
import numpy as np
import joblib
import sklearn
from google.cloud import storage, aiplatform
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==============================================================================
# CONFIGURAÇÕES
# ==============================================================================
BUCKET_NAME = 'brazil-soccer-data'
PROJECT_ID = "project-f38402f0-f3e4-4629-a39"
REGION = "southamerica-east1"
MODEL_DIR = "modelo_futebol_linear"
MODEL_FILENAME = "model.joblib"

# --- TRAVA DE SEGURANÇA ---
if not sklearn.__version__.startswith("1.3"):
    raise ValueError("PARE! Você precisa reiniciar o Kernel após o pip install scikit-learn==1.3.2")

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
    conditions = [
        (df['home_team_goal_count'] > df['away_team_goal_count']),
        (df['home_team_goal_count'] == df['away_team_goal_count']),
        (df['home_team_goal_count'] < df['away_team_goal_count'])
    ]
    df['target'] = np.select(conditions, [0, 1, 2])
    return df

def main():
    # 1. Carregamento e Processamento
    df = load_data_from_gcs(BUCKET_NAME)
    df = preprocess_data(df)
    
    # 2. Features
    features = [
        'Pre-Match PPG (Home)', 'Pre-Match PPG (Away)',
        'home_ppg', 'away_ppg',
        'average_goals_per_match_pre_match',
        'odds_ft_home_team_win', 'odds_ft_draw', 'odds_ft_away_team_win'
    ]
    
    df_clean = df.dropna(subset=features)
    X = df_clean[features]
    y = df_clean['target']
    
    # 3. Divisão
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # 4. Treinamento
    model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=2000)
    model.fit(X_train.values, y_train)
    
    # 5. Avaliação
    acc = accuracy_score(y_val, model.predict(X_val.values))
    
    # 6. Salvar Localmente
    joblib.dump(model, MODEL_FILENAME)
    
    # 7. Upload GCS
    bucket = storage.Client().bucket(BUCKET_NAME)
    blob = bucket.blob(f"{MODEL_DIR}/{MODEL_FILENAME}")
    blob.upload_from_filename(MODEL_FILENAME)
    
    # 8. Deploy no Vertex AI
    aiplatform.init(project=PROJECT_ID, location=REGION)

    # Imagem compatível com a versão 1.3 que instalamos
    model_vertex = aiplatform.Model.upload(
        display_name="futebol-linear-v3-final",
        artifact_uri=f"gs://{BUCKET_NAME}/{MODEL_DIR}/",
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-3:latest"
    )

    # Se o Endpoint anterior falhou, criamos um novo para garantir
    endpoint = model_vertex.deploy(
        machine_type="n1-standard-2",
        min_replica_count=1,
        max_replica_count=1
    )