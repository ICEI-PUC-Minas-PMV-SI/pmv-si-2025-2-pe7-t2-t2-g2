import streamlit as st
import pandas as pd
from google.cloud import aiplatform

# --- CONFIGURAÇÃO ---
ENDPOINT_RESOURCE_NAME = "projects/12971905854/locations/southamerica-east1/endpoints/8061852351318720512"
PROJECT_ID = "project-f38402f0-f3e4-4629-a39"
REGION = "southamerica-east1"

def get_prediction(features_list):
    """Envia os dados para o Vertex AI e recebe a previsão."""
    aiplatform.init(project=PROJECT_ID, location=REGION)
    endpoint = aiplatform.Endpoint(ENDPOINT_RESOURCE_NAME)
    
    instances_payload = [features_list]
    
    response = endpoint.predict(instances=instances_payload)
    return response.predictions[0]

# --- INTERFACE (FRONTEND) ---
st.set_page_config(page_title="Previsor de Futebol AI", page_icon="⚽", layout="centered")

st.title("⚽ Previsor de Resultados: Brasileirão")
st.markdown("Insira os dados pré-jogo para consultar o oráculo (Modelo XGBoost no Vertex AI).")

# Criando colunas para organizar o input
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Time da Casa")
    ppg_home = st.number_input("Pontos Por Jogo (PPG) - Casa", 0.0, 3.0, 1.50, 0.01)
    home_ppg_season = st.number_input("Média PPG Temporada - Casa", 0.0, 3.0, 1.60, 0.01)
    
with col2:
    st.subheader("✈️ Time Visitante")
    ppg_away = st.number_input("Pontos Por Jogo (PPG) - Visitante", 0.0, 3.0, 1.00, 0.01)
    away_ppg_season = st.number_input("Média PPG Temporada - Visitante", 0.0, 3.0, 0.80, 0.01)

st.divider()

st.subheader("💰 Odds e Estatísticas")
c1, c2, c3 = st.columns(3)
odd_home = c1.number_input("Odd Vitória Casa", 1.0, 20.0, 1.90, 0.01)
odd_draw = c2.number_input("Odd Empate", 1.0, 20.0, 3.20, 0.01)
odd_away = c3.number_input("Odd Vitória Visitante", 1.0, 20.0, 4.50, 0.01)

avg_goals = st.slider("Média de Gols em confrontos anteriores", 0.0, 5.0, 2.5, 0.1)

# Botão de Previsão
if st.button("🔮 Prever Resultado", type="primary"):
    
    features_clean = [
        float(ppg_home), 
        float(ppg_away), 
        float(home_ppg_season), 
        float(away_ppg_season), 
        float(avg_goals), 
        float(odd_home), 
        float(odd_draw), 
        float(odd_away)
    ]
    
    with st.spinner('Consultando o cérebro do modelo na nuvem...'):
        try:
            # Enviamos a lista limpa
            probs = get_prediction(features_clean)
            
            # --- Exibição dos Resultados ---
            st.success("Previsão Realizada com Sucesso!")
            st.markdown("---")
            
            # Layout de métricas
            col_res1, col_res2, col_res3 = st.columns(3)
            
            max_prob = max(probs)
            
            col_res1.metric("🏠 Vitória Casa", f"{probs[0]:.1%}", delta="Favorito" if probs[0] == max_prob else None)
            col_res2.metric("⚖️ Empate", f"{probs[1]:.1%}", delta="Provável" if probs[1] == max_prob else None)
            col_res3.metric("✈️ Vitória Visitante", f"{probs[2]:.1%}", delta="Zebra?" if probs[2] == max_prob else None)
            
            # Veredito Final
            winner_idx = probs.index(max_prob)
            labels = ["Vitória do Mandante", "Empate", "Vitória do Visitante"]
            
            st.markdown("### Veredito:")
            if max_prob > 0.60:
                st.info(f"🏆 O modelo está confiante na **{labels[winner_idx]}**")
            else:
                st.warning(f"⚠️ Jogo difícil! O modelo sugere **{labels[winner_idx]}**, mas a certeza é baixa.")
            
        except Exception as e:
            st.error(f"Erro ao conectar com o Vertex AI.")
            st.warning("Detalhes técnicos para debug:")
            st.code(str(e))
