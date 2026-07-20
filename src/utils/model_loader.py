"""
Model Loader
------------
Loads all saved machine learning artifacts.
"""

import joblib

from config.paths import MODELS_DIR
from config.logging_config import logger


def load_model():
    """
    Load trained machine learning model.
    """

    model_path = MODELS_DIR / "best_model.pkl"

    try:

        model = joblib.load(model_path)

        logger.info("Best model loaded successfully.")

        return model

    except FileNotFoundError:

        logger.error(f"Model not found : {model_path}")

        raise


def load_scaler():
    """
    Load feature scaler.
    """

    scaler_path = MODELS_DIR / "scaler.pkl"

    try:

        scaler = joblib.load(scaler_path)

        logger.info("Scaler loaded successfully.")

        return scaler

    except FileNotFoundError:

        logger.error(f"Scaler not found : {scaler_path}")

        raise


def load_feature_columns():
    """
    Load feature column names.
    """

    feature_path = MODELS_DIR / "feature_columns.pkl"

    try:

        feature_columns = joblib.load(feature_path)

        logger.info("Feature columns loaded successfully.")

        return feature_columns

    except FileNotFoundError:

        logger.error(f"Feature columns not found : {feature_path}")

        raise