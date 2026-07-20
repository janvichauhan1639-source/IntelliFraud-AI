"""
Load Dataset Module
-------------------
This module loads the financial fraud dataset.
"""

from pathlib import Path
import pandas as pd

from config.paths import RAW_DATA_PATH
from config.logging_config import logger


def load_dataset() -> pd.DataFrame:
    """
    Load the raw dataset.

    Returns:
        pd.DataFrame: Loaded dataset.
    """

    try:
        logger.info("Loading dataset...")

        if not RAW_DATA_PATH.exists():
            raise FileNotFoundError(
                f"Dataset not found: {RAW_DATA_PATH}"
            )

        df = pd.read_csv(RAW_DATA_PATH)

        logger.info("Dataset loaded successfully.")
        logger.info(f"Shape: {df.shape}")

        return df

    except Exception as e:
        logger.error(f"Error loading dataset: {e}")
        raise