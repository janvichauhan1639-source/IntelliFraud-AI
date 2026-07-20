"""
Reports Center
--------------
Download Reports, Models and Project Artifacts
"""

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Reports & Download Center")

st.markdown("""
Download all project reports, trained models,
processed datasets and machine learning artifacts.
""")

st.divider()

comparison = Path("reports/model_comparison.csv")
dataset = Path("data/processed/cleaned_data.csv")
model = Path("models/best_model.pkl")
scaler = Path("models/scaler.pkl")
features = Path("models/feature_columns.pkl")
metadata = Path("models/metadata.json")

st.subheader("📊 Project Artifacts")

files = [
    comparison,
    dataset,
    model,
    scaler,
    features,
    metadata
]

available = sum(f.exists() for f in files)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Artifacts",
        len(files)
    )

with c2:
    st.metric(
        "Available",
        available
    )

with c3:
    st.metric(
        "Missing",
        len(files) - available
    )

st.divider()

def download_card(title, path, filename):

    st.subheader(title)

    if path.exists():

        with open(path, "rb") as f:

            st.success("Available")

            st.download_button(
                f"⬇ Download {filename}",
                data=f,
                file_name=filename,
                use_container_width=True
            )

    else:

        st.error("File not found")

left, right = st.columns(2)

with left:

    download_card(
        "📊 Model Comparison",
        comparison,
        "model_comparison.csv"
    )

    download_card(
        "🧹 Clean Dataset",
        dataset,
        "cleaned_data.csv"
    )

    download_card(
        "🤖 Best Model",
        model,
        "best_model.pkl"
    )

with right:

    download_card(
        "⚙️ Scaler",
        scaler,
        "scaler.pkl"
    )

    download_card(
        "📋 Feature Columns",
        features,
        "feature_columns.pkl"
    )

    download_card(
        "📑 Metadata",
        metadata,
        "metadata.json"
    )

st.divider()
st.subheader("📦 Artifact Status")

status = {
    "Model Comparison": comparison.exists(),
    "Clean Dataset": dataset.exists(),
    "Best Model": model.exists(),
    "Scaler": scaler.exists(),
    "Feature Columns": features.exists(),
    "Metadata": metadata.exists()
}

for name, ok in status.items():

    if ok:
        st.success(f"✅ {name}")
    else:
        st.error(f"❌ {name}")

st.divider()
st.info("""
All downloadable artifacts are generated automatically
after successful model training and evaluation.

These files can be used for deployment, analysis,
and future model retraining.
""")