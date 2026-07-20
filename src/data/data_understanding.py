"""
Data Understanding Module
---------------------------------
Performs initial inspection of the dataset.
"""

import pandas as pd
from config.logging_config import logger
from config.paths import RAW_DATA_PATH


def understand_dataset():
    logger.info("Loading dataset...")

    df = pd.read_csv(RAW_DATA_PATH)

    print("=" * 70)
    print("DATASET OVERVIEW")
    print("=" * 70)

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nClass Distribution")
    print(df["Class"].value_counts())

    print("\nFraud Percentage")

    fraud_percentage = (
        df["Class"].value_counts(normalize=True) * 100
    )

    print(fraud_percentage)

    print("\nFirst Five Rows")
    print(df.head())

    logger.info("Dataset Understanding Completed.")

    return df