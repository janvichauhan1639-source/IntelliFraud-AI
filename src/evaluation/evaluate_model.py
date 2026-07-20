"""
Model Evaluation Module
-----------------------
Evaluates all trained models using multiple metrics.
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained model.
    """

    predictions = model.predict(X_test)

    metrics = {

        "Accuracy": accuracy_score(y_test, predictions),

        "Precision": precision_score(y_test, predictions),

        "Recall": recall_score(y_test, predictions),

        "F1 Score": f1_score(y_test, predictions),

        "ROC AUC": roc_auc_score(y_test, predictions),

        "Confusion Matrix": confusion_matrix(y_test, predictions),

        "Classification Report":
        classification_report(y_test, predictions)

    }

    return metrics