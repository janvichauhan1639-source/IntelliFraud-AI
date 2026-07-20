"""
Feature Engineering Module
--------------------------
Performs feature scaling on numerical features.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

from config.logging_config import logger


def scale_features(X_train: pd.DataFrame, X_test: pd.DataFrame):
    """
    Scale Time and Amount columns.

    Args:
        X_train: Training features
        X_test: Testing features

    Returns:
        X_train_scaled, X_test_scaled, scaler
    """

    logger.info("=" * 60)
    logger.info("FEATURE SCALING STARTED")
    logger.info("=" * 60)

    scaler = StandardScaler()

    columns_to_scale = ["Time", "Amount"]

    X_train = X_train.copy()
    X_test = X_test.copy()

    X_train[columns_to_scale] = scaler.fit_transform(
        X_train[columns_to_scale]
    )

    X_test[columns_to_scale] = scaler.transform(
        X_test[columns_to_scale]
    )

    logger.info("Feature Scaling Completed Successfully")

    logger.info("=" * 60)
    logger.info("FEATURE SCALING COMPLETED")
    logger.info("=" * 60)

    return X_train, X_test, scaler