"""
Data Splitting Module
---------------------
Splits the cleaned dataset into training and testing sets.
"""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from config.settings import TARGET_COLUMN, TEST_SIZE, RANDOM_STATE
from config.logging_config import logger


def split_dataset(df: pd.DataFrame):
    """
    Split dataset into train and test sets
    and save them into data/processed.
    """

    logger.info("=" * 60)
    logger.info("TRAIN TEST SPLITTING STARTED")
    logger.info("=" * 60)

    # -----------------------------
    # Split Features and Target
    # -----------------------------
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    logger.info(f"X Train Shape : {X_train.shape}")
    logger.info(f"X Test Shape  : {X_test.shape}")

    logger.info(f"y Train Shape : {y_train.shape}")
    logger.info(f"y Test Shape  : {y_test.shape}")

    # ---------------------------------
    # Create processed directory
    # ---------------------------------

    processed_dir = Path("data") / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    # ---------------------------------
    # Merge X and y
    # ---------------------------------

    train_df = X_train.copy()
    train_df[TARGET_COLUMN] = y_train.values

    test_df = X_test.copy()
    test_df[TARGET_COLUMN] = y_test.values

    # ---------------------------------
    # Save CSV Files
    # ---------------------------------

    train_path = processed_dir / "train.csv"
    test_path = processed_dir / "test.csv"

    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    logger.info(f"Train CSV Saved : {train_path}")
    logger.info(f"Test CSV Saved  : {test_path}")

    logger.info("=" * 60)
    logger.info("TRAIN TEST SPLITTING COMPLETED")
    logger.info("=" * 60)

    return X_train, X_test, y_train, y_test