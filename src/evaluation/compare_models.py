"""
Model Comparison Module
-----------------------
Compares all trained models based on F1 Score.
"""

import pandas as pd


def compare_models(results):

    comparison = []

    for model_name, result in results.items():

        metrics = result["metrics"]

        comparison.append({

            "Model": model_name,
            "Accuracy": metrics["Accuracy"],
            "Precision": metrics["Precision"],
            "Recall": metrics["Recall"],
            "F1 Score": metrics["F1 Score"],
            "ROC AUC": metrics["ROC AUC"]

        })

    comparison_df = pd.DataFrame(comparison)

    comparison_df = comparison_df.sort_values(
        by="F1 Score",
        ascending=False
    )

    return comparison_df