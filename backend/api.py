"""
AI Powered Financial Fraud Detection API
----------------------------------------
FastAPI Backend
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.prediction import predict_transaction
app = FastAPI(
    title="AI Powered Financial Fraud Detection API",
    description="Enterprise Machine Learning API for detecting fraudulent financial transactions.",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):

    Time: float

    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float

    Amount: float

@app.get("/")
def root():

    return {
        "message": "AI Powered Financial Fraud Detection API Running",
        "status": "online",
        "version": "1.0.0"
    }
@app.get("/health")
def health():

    return {
        "status": "healthy",
        "backend": "online",
        "model": "loaded"
    }

@app.get("/info")
def info():

    return {

        "project": "AI Powered Financial Fraud Detection",

        "framework": "FastAPI",

        "machine_learning": "Scikit-Learn",

        "frontend": "Streamlit",

        "best_model": "Random Forest"

    }

@app.post("/predict")
def predict(transaction: Transaction):

    result = predict_transaction(
        transaction.model_dump()
    )

    return result