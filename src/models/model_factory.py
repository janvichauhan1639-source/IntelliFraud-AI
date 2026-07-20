"""
Model Factory
-------------
Returns all machine learning models.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def get_models():
    """
    Returns dictionary of ML models.
    """

    models = {

        "Logistic Regression": LogisticRegression(
            random_state=42,
            max_iter=1000
        ),

        "Decision Tree": DecisionTreeClassifier(
            random_state=42
        ),

        "Random Forest": RandomForestClassifier(
            random_state=42,
            n_estimators=100
        ),

        "XGBoost": XGBClassifier(
            random_state=42,
            eval_metric="logloss"
        )

    }

    return models