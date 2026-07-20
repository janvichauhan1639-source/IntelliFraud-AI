"""
AI Powered Financial Fraud Detection System
-------------------------------------------
Main Entry Point
"""

from pathlib import Path

from src.data.data_understanding import understand_dataset
from src.data.validate_data import validate_dataset

from src.preprocessing.clean_data import clean_dataset
from src.preprocessing.split_data import split_dataset
from src.preprocessing.feature_engineering import scale_features

from src.models.train_model import train_models

from src.evaluation.compare_models import compare_models
from src.evaluation.save_best_model import save_best_model
from src.evaluation.save_artifacts import save_artifacts


def main():

    print("=" * 80)
    print(" AI POWERED FINANCIAL FRAUD DETECTION SYSTEM ")
    print("=" * 80)
    print("\n[STEP 1] DATA UNDERSTANDING")

    df = understand_dataset()

    print("\n[STEP 2] DATA VALIDATION")

    validate_dataset(df)
    print("\n[STEP 3] DATA CLEANING")

    df = clean_dataset(df)

    print("\n[STEP 4] TRAIN TEST SPLIT")

    X_train, X_test, y_train, y_test = split_dataset(df)

    print("\n[STEP 5] FEATURE SCALING")

    X_train, X_test, scaler = scale_features(
        X_train,
        X_test
    )

    print("\n[STEP 6] MODEL TRAINING")

    results = train_models(
        X_train,
        X_test,
        y_train,
        y_test
    )

    print("\n")
    print("=" * 80)
    print("MODEL COMPARISON")
    print("=" * 80)

    comparison = compare_models(results)

    print(comparison)
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    comparison.to_csv(
        reports_dir / "model_comparison.csv",
        index=False
    )

    print("\nModel comparison saved successfully.")

    best_model_name, best_score = save_best_model(results)

    print("\n")
    print("=" * 80)
    print("BEST MODEL")
    print("=" * 80)

    print(f"Model    : {best_model_name}")
    print(f"F1 Score : {best_score:.4f}")

    best_model = results[best_model_name]["model"]

    save_artifacts(
        best_model=best_model,
        scaler=scaler,
        feature_columns=X_train.columns.tolist()
    )
    print("\n")
    print("=" * 80)
    print("PIPELINE EXECUTED SUCCESSFULLY")
    print("=" * 80)

    print("\nGenerated Files")

    print("✔ reports/model_comparison.csv")
    print("✔ models/best_model.pkl")
    print("✔ models/scaler.pkl")
    print("✔ models/feature_columns.pkl")
    print("✔ models/metadata.json")

    print("\nProject Completed Successfully!")


if __name__ == "__main__":
    main()