"""
Model Training Module
---------------------
Trains and evaluates multiple machine learning models.
"""

from config.logging_config import logger
from src.models.model_factory import get_models
from src.evaluation.evaluate_model import evaluate_model


def train_models(X_train, X_test, y_train, y_test):
    """
    Train and evaluate all machine learning models.

    Args:
        X_train: Training features
        X_test: Testing features
        y_train: Training labels
        y_test: Testing labels

    Returns:
        dict: Evaluation metrics for all models.
    """

    logger.info("=" * 70)
    logger.info("MODEL TRAINING STARTED")
    logger.info("=" * 70)

    models = get_models()

    results = {}

    for name, model in models.items():

        logger.info(f"\nTraining {name}...")

        # Train Model
        model.fit(X_train, y_train)

        # Evaluate Model
        metrics = evaluate_model(
            model=model,
            X_test=X_test,
            y_test=y_test
        )

        # Store trained model and metrics
        results[name] = {
            "model": model,
            "metrics": metrics
        }

        logger.info(f"Model : {name}")
        logger.info(f"Accuracy  : {metrics['Accuracy']:.4f}")
        logger.info(f"Precision : {metrics['Precision']:.4f}")
        logger.info(f"Recall    : {metrics['Recall']:.4f}")
        logger.info(f"F1 Score  : {metrics['F1 Score']:.4f}")
        logger.info(f"ROC AUC   : {metrics['ROC AUC']:.4f}")

    logger.info("=" * 70)
    logger.info("MODEL TRAINING COMPLETED")
    logger.info("=" * 70)

    return results