import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Home",
    layout="wide"
)

def load_css():
    ...
    
load_css()



"""
Prediction Module
-----------------
Predict fraud transactions using trained model.
"""

import pandas as pd

from src.utils.model_loader import (
    load_model,
    load_scaler
)

model = load_model()
scaler = load_scaler()


def predict_transaction(data: dict):
    """
    Predict a single transaction.
    """

    df = pd.DataFrame([data])

    # Scale only Time and Amount
    columns_to_scale = ["Time", "Amount"]

    df[columns_to_scale] = scaler.transform(
        df[columns_to_scale]
    )

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {

        "prediction": int(prediction),

        "label": (
            "Fraud"
            if prediction == 1
            else "Legitimate"
        ),

        "fraud_probability": round(
            probability * 100,
            2
        ),

        "confidence": round(
            max(probability, 1 - probability) * 100,
            2
        )

    }