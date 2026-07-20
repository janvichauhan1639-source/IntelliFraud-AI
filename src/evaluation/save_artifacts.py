"""
Save ML Artifacts
-----------------
Saves trained model, scaler and feature metadata.
"""

import json
import joblib

from config.paths import MODELS_DIR


def save_artifacts(best_model,
                   scaler,
                   feature_columns):

    MODELS_DIR.mkdir(exist_ok=True)

    joblib.dump(
        best_model,
        MODELS_DIR / "best_model.pkl"
    )

    joblib.dump(
        scaler,
        MODELS_DIR / "scaler.pkl"
    )

    joblib.dump(
        feature_columns,
        MODELS_DIR / "feature_columns.pkl"
    )

    metadata = {

        "total_features": len(feature_columns),
        "feature_names": feature_columns

    }

    with open(
        MODELS_DIR / "metadata.json",
        "w"
    ) as f:

        json.dump(metadata, f, indent=4)

    print("\nArtifacts Saved Successfully")