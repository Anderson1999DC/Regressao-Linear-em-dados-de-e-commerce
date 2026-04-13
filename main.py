from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

modelo = joblib.load("modelo_ecommerce.pkl")
colunas = joblib.load("colunas_ecommerce.pkl")

app = FastAPI(
    title="API — Previsão de Gasto em E-commerce",
    description="Modelo de Regressão Linear treinado com dados de clientes de e-commerce de moda",
    version="1.0.0"
)

class Cliente(BaseModel):
    avg_session_length: float
    time_on_app: float
    time_on_website: float
    length_of_membership: float

@app.get("/")
def root():
    return {"status": "online", "modelo": "Regressão Linear", "versao": "1.0.0"}

@app.get("/app", response_class=HTMLResponse)
def interface():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/predict")
def predict(cliente: Cliente):
    dados = {
        "Avg. Session Length": cliente.avg_session_length,
        "Time on App": cliente.time_on_app,
        "Time on Website": cliente.time_on_website,
        "Length of Membership": cliente.length_of_membership
    }

    df = pd.DataFrame([dados])
    df_final = df.reindex(columns=colunas, fill_value=0)
    gasto = modelo.predict(df_final)[0]

    return {
        "gasto_anual_previsto": round(float(gasto), 2),
        "unidade": "USD",
        "modelo": "LinearRegression"
    }