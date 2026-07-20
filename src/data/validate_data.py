"""
Data Validation Module
----------------------
Validates the quality of the dataset before preprocessing.
"""

import pandas as pd

from config.logging_config import logger
from config.settings import TARGET_COLUMN


def validate_dataset(df: pd.DataFrame) -> bool:
    """
    Validate dataset before preprocessing.

    Args:
        df (pd.DataFrame): Input dataframe.

    Returns:
        bool: True if validation passes.
    """

    logger.info("=" * 60)
    logger.info("DATA VALIDATION STARTED")
    logger.info("=" * 60)
    logger.info(f"Dataset Shape : {df.shape}")

    missing = df.isnull().sum().sum()
    logger.info(f"Total Missing Values : {missing}")
    duplicates = df.duplicated().sum()
    logger.info(f"Duplicate Rows : {duplicates}")
    if TARGET_COLUMN not in df.columns:
        raise ValueError(f"{TARGET_COLUMN} column not found.")

    logger.info(f"Target Column : {TARGET_COLUMN}")
    logger.info("\nData Types")
    logger.info(df.dtypes)
    logger.info("\nClass Distribution")
    logger.info(df[TARGET_COLUMN].value_counts())

    logger.info("=" * 60)
    logger.info("DATA VALIDATION COMPLETED")
    logger.info("=" * 60)

    return True