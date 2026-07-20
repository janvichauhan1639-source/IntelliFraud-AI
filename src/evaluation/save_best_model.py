"""
Save Best Model
"""

import joblib

from config.paths import MODELS_DIR


def save_best_model(results):

    MODELS_DIR.mkdir(exist_ok=True)

    best_name = None
    best_score = -1
    best_model = None

    for model_name, result in results.items():

        f1 = result["metrics"]["F1 Score"]

        if f1 > best_score:

            best_score = f1
            best_name = model_name
            best_model = result["model"]

    joblib.dump(
        best_model,
        MODELS_DIR / "best_model.pkl"
    )

    return best_name, best_score