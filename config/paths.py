"""
Project Path Configuration
--------------------------
Centralized file and folder paths used across the project.
"""

from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SAMPLE_DATA_DIR = DATA_DIR / "sample"
RAW_DATA_PATH = RAW_DATA_DIR / "creditcard.csv"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"
ASSETS_DIR = PROJECT_ROOT / "assets"
FRONTEND_DIR = PROJECT_ROOT / "frontend"
BACKEND_DIR = PROJECT_ROOT / "backend"
DOCS_DIR = PROJECT_ROOT / "docs"