"""
Reports Center
--------------
Download Reports, Models and Project Artifacts
"""

from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

BASE = Path(__file__).resolve().parents[2]

st.title("📄 Reports & Download Center")

st.markdown("""
Download all project reports, trained models,
sample datasets and machine learning artifacts.
""")

st.divider()

comparison = BASE / "reports" / "model_comparison.csv"

# Dataset (sample first, processed fallback)
sample_dataset = BASE / "data" / "sample" / "sample_transactions.csv"
processed_dataset = BASE / "data" / "processed" / "cleaned_data.csv"

if sample_dataset.exists():
    dataset = sample_dataset
elif processed_dataset.exists():
    dataset = processed_dataset
else:
    dataset = sample_dataset

model = BASE / "models" / "best_model.pkl"
scaler = BASE / "models" / "scaler.pkl"
features = BASE / "models" / "feature_columns.pkl"
metadata = BASE / "models" / "metadata.json"

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
    st.metric("Artifacts", len(files))

with c2:
    st.metric("Available", available)

with c3:
    st.metric("Missing", len(files) - available)

st.divider()


def download_card(title, path, filename):

    st.subheader(title)

    if path.exists():

        st.success("Available")

        with open(path, "rb") as f:

            st.download_button(
                label=f"⬇ Download {filename}",
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
        "🧹 Sample Dataset",
        dataset,
        dataset.name
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
    "Dataset": dataset.exists(),
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

The sample dataset is included for live demo purposes,
while the full processed dataset can be generated locally
using:

python run.py
""")