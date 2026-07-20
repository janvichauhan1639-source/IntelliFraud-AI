"""
Model Performance Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

report_path = Path("reports/model_comparison.csv")

if not report_path.exists():
    st.error("Model comparison report not found.")
    st.stop()

df = pd.read_csv(report_path)

st.title("📊 Machine Learning Model Performance")

st.markdown("""
Compare all trained Machine Learning models using
Accuracy, Precision, Recall, F1 Score and ROC-AUC.
""")

st.divider()

best_model = df.sort_values(
    "F1 Score",
    ascending=False
).iloc[0]

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "🏆 Best Model",
        best_model["Model"]
    )

with c2:
    st.metric(
        "F1 Score",
        f"{best_model['F1 Score']:.4f}"
    )

with c3:
    st.metric(
        "Accuracy",
        f"{best_model['Accuracy']:.4f}"
    )

st.divider()

st.subheader("Model Comparison")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

metric = st.selectbox(
    "Select Metric",
    [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"
    ]
)

fig = px.bar(
    df,
    x="Model",
    y=metric,
    text=metric,
    color=metric,
    title=f"{metric} Comparison"
)

fig.update_traces(texttemplate="%{text:.4f}")

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("Best Model Performance")

radar = px.line_polar(

    r=[
        best_model["Accuracy"],
        best_model["Precision"],
        best_model["Recall"],
        best_model["F1 Score"],
        best_model["ROC AUC"]
    ],

    theta=[
        "Accuracy",
        "Precision",
        "Recall",
        "F1",
        "ROC AUC"
    ],

    line_close=True
)

st.plotly_chart(
    radar,
    use_container_width=True
)

st.divider()

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Model Comparison",
    csv,
    "model_comparison.csv",
    "text/csv",
    use_container_width=True
)

st.divider()

st.success(f"""
### 🏆 Best Performing Model

**{best_model['Model']}**

Accuracy : **{best_model['Accuracy']:.4f}**

Precision : **{best_model['Precision']:.4f}**

Recall : **{best_model['Recall']:.4f}**

F1 Score : **{best_model['F1 Score']:.4f}**

ROC-AUC : **{best_model['ROC AUC']:.4f}**

This model is recommended for deployment because it provides the best balance between fraud detection and false positive control.
""")