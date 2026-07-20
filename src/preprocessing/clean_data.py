"""
Data Cleaning Module
--------------------
Cleans the raw dataset and saves the processed dataset.
"""

import pandas as pd

from config.paths import PROCESSED_DATA_DIR
from config.logging_config import logger


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset.

    Args:
        df (pd.DataFrame): Raw dataset

    Returns:
        pd.DataFrame: Cleaned dataset
    """

    logger.info("=" * 60)
    logger.info("DATA CLEANING STARTED")
    logger.info("=" * 60)

    original_rows = len(df)

    # Remove duplicate rows
    df = df.drop_duplicates()

    cleaned_rows = len(df)
    removed_rows = original_rows - cleaned_rows

    logger.info(f"Original Rows : {original_rows}")
    logger.info(f"Rows Removed  : {removed_rows}")
    logger.info(f"Final Rows    : {cleaned_rows}")

    # Create processed directory if it doesn't exist
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_file = PROCESSED_DATA_DIR / "cleaned_data.csv"

    df.to_csv(output_file, index=False)

    logger.info(f"Clean dataset saved to: {output_file}")

    logger.info("=" * 60)
    logger.info("DATA CLEANING COMPLETED")
    logger.info("=" * 60)

    return df