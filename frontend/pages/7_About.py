"""
About Project
-------------
AI Powered Financial Fraud Detection System
"""

import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ AI Powered Financial Fraud Detection System")

st.markdown("""
### Enterprise Machine Learning Solution for Real-Time Financial Fraud Detection

This platform leverages Artificial Intelligence and Machine Learning to
identify fraudulent financial transactions with high accuracy, enabling
financial institutions to reduce fraud losses and improve transaction security.
""")

st.divider()

st.subheader("📖 Project Overview")

st.info("""
This project is an end-to-end Machine Learning application that covers the
complete lifecycle of fraud detection.

✔ Data Understanding

✔ Data Validation

✔ Data Cleaning

✔ Feature Engineering

✔ Machine Learning Model Training

✔ Model Evaluation

✔ FastAPI REST API

✔ Streamlit Interactive Dashboard

✔ Real-Time Prediction

✔ Batch Prediction

✔ Analytics & Reporting
""")

st.divider()
left, right = st.columns(2)

with left:

    st.subheader("🎯 Project Objectives")

    st.markdown("""
- Detect fraudulent transactions in real time
- Reduce financial losses
- Improve banking security
- Provide AI-powered decision support
- Build an enterprise-grade fraud detection platform
""")

with right:

    st.subheader("🚀 Key Features")

    st.markdown("""
- 🔍 Single Transaction Prediction
- 📂 Batch Prediction
- 📊 Interactive Dashboard
- 📈 Advanced Analytics
- 📉 Model Performance Comparison
- 📄 Downloadable Reports
- ⚡ FastAPI REST API
- 🎨 Interactive Streamlit UI
""")

st.divider()

st.subheader("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.success("""
### 🤖 Machine Learning

- Python
- Scikit-Learn
- Random Forest
- Decision Tree
- Logistic Regression
- StandardScaler
""")

with tech2:

    st.success("""
### ⚙ Backend

- FastAPI
- Uvicorn
- Pydantic
- Joblib
- REST API
""")

with tech3:

    st.success("""
### 🎨 Frontend

- Streamlit
- Plotly
- Pandas
- NumPy
- Interactive Dashboard
""")

st.divider()

st.subheader("📊 Dataset Information")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Transactions",
        "284,807"
    )

with c2:
    st.metric(
        "Fraud Cases",
        "492"
    )

with c3:
    st.metric(
        "Features",
        "30"
    )

with c4:
    st.metric(
        "Target",
        "Class"
    )

st.divider()

st.subheader("🏆 Best Machine Learning Model")

st.success("""
### Random Forest Classifier

✔ Accuracy : 99.95%

✔ High Precision

✔ High Recall

✔ Excellent F1 Score

✔ Production Ready
""")

st.divider()

st.subheader("📂 Project Modules")

modules = [
    "🏠 Home",
    "📊 Dashboard",
    "🔍 Single Prediction",
    "📂 Batch Prediction",
    "📈 Analytics",
    "📉 Model Performance",
    "📄 Reports",
    "⚙ Settings",
    "🚀 FastAPI Backend"
]

for module in modules:
    st.success(module)

st.divider()

st.subheader("🚀 Future Enhancements")

st.info("""
• Deep Learning Models

• Explainable AI (SHAP)

• User Authentication

• Cloud Deployment (AWS/Azure)

• Docker & Kubernetes

• Real-Time Streaming Fraud Detection

• Email & SMS Alerts

• Continuous Model Retraining
""")

st.divider()

st.markdown(
"""
<div style="text-align:center;padding:20px">

<h3>🛡 AI Powered Financial Fraud Detection System</h3>

<p>
Enterprise Machine Learning Platform
</p>

<p>
Python • Scikit-Learn • FastAPI • Streamlit • Plotly
</p>

<p>
Version 1.0.0
</p>

</div>
""",
unsafe_allow_html=True
)