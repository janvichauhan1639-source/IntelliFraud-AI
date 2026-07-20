"""
Data Splitting Module
---------------------
Splits the cleaned dataset into training and testing sets.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

from config.settings import TARGET_COLUMN, TEST_SIZE, RANDOM_STATE
from config.logging_config import logger

def split_dataset(df: pd.DataFrame):
    """
    Split dataset into train and test sets.
    """

    logger.info("=" * 60)
    logger.info("TRAIN TEST SPLITTING STARTED")
    logger.info("=" * 60)

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

    logger.info("=" * 60)
    logger.info("TRAIN TEST SPLITTING COMPLETED")
    logger.info("=" * 60)

    return X_train, X_test, y_train, y_test