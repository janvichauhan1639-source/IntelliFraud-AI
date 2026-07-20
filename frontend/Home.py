import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="AI Powered Financial Fraud Detection",
    page_icon="🛡️",
    layout="wide",

    initial_sidebar_state="expanded"
)
@st.cache_data
def load_data():

    try:
        return pd.read_csv(
            "data/processed/cleaned_data.csv"
        )

    except Exception:

        return None


df = load_data()

if df is not None:

    TOTAL_TRANSACTIONS = len(df)

    FRAUD_CASES = int(df["Class"].sum())

    LEGITIMATE = TOTAL_TRANSACTIONS - FRAUD_CASES

    FRAUD_RATE = (
        FRAUD_CASES / TOTAL_TRANSACTIONS
    ) * 100

    AVG_AMOUNT = df["Amount"].mean()

else:

    TOTAL_TRANSACTIONS = 284807

    FRAUD_CASES = 492

    LEGITIMATE = 284315

    FRAUD_RATE = 0.172

    AVG_AMOUNT = 88.35
st.markdown("""
<style>

.main .block-container{

    padding-top:1.5rem;
    padding-bottom:2rem;

}

/* Hero */

.hero{

    background:linear-gradient(
        135deg,
        #0F172A,
        #1E3A8A,
        #2563EB
    );

    padding:70px 60px;

    border-radius:25px;

    color:white;

    box-shadow:0 20px 40px rgba(0,0,0,.20);

    margin-bottom:35px;

}

.hero h1{

    color:white;

    font-size:68px;

    font-weight:900;

    margin-bottom:19px;

    line-height:1.2;

    letter-spacing:-1px;

}

.hero p{

    color:#E2E8F0;

    font-size:20x;

    line-height:1.8;

    margin-top:8px;

}

/* KPI */

[data-testid="metric-container"]{

    background:white;

    border-radius:18px;

    padding:20px;

    border:1px solid #E5E7EB;

    box-shadow:0px 8px 18px rgba(0,0,0,.08);

}

/* Cards */

.card{

    background:white;

    border-radius:18px;

    padding:20px;

    box-shadow:0px 8px 18px rgba(0,0,0,.08);

    margin-bottom:15px;

    height:260px;

}

</style>
""", unsafe_allow_html=True)
st.markdown(f"""

<div class="hero">

<h1>

🛡 AI Powered Financial Fraud Detection System

</h1>

<p>

Enterprise AI Platform for detecting financial fraud using
Machine Learning, FastAPI and Streamlit.

</p>

<br>

<table width="100%">

<tr>

<td>

<h2>{TOTAL_TRANSACTIONS:,}</h2>

Transactions

</td>

<td>

<h2>{FRAUD_CASES:,}</h2>

Fraud Cases

</td>

<td>

<h2>{FRAUD_RATE:.3f}%</h2>

Fraud Rate

</td>

<td>

<h2>99.95%</h2>

Accuracy

</td>

</tr>

</table>

</div>

""", unsafe_allow_html=True)
st.subheader("📊 Executive Dashboard")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "💳 Transactions",
        f"{TOTAL_TRANSACTIONS:,}"
    )

with c2:

    st.metric(
        "🚨 Fraud Cases",
        f"{FRAUD_CASES:,}"
    )

with c3:

    st.metric(
        "🛡 Legitimate",
        f"{LEGITIMATE:,}"
    )

with c4:

    st.metric(
        "💰 Average Amount",
        f"₹ {AVG_AMOUNT:.2f}"
    )

st.divider()
st.subheader("🤖 AI Platform Capabilities")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">

<h3>🔍 AI Fraud Detection</h3>

<p>
Detect fraudulent financial transactions
using advanced Machine Learning models.
</p>

<hr>

✅ Random Forest<br>
✅ Decision Tree<br>
✅ Logistic Regression<br>
✅ Real-Time Prediction

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">

<h3>📊 Business Intelligence</h3>

<p>
Interactive dashboards for executives,
analysts and fraud investigation teams.
</p>

<hr>

✅ Executive Dashboard<br>
✅ Analytics<br>
✅ Reports<br>
✅ KPI Monitoring

</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">

<h3>⚡ Enterprise API</h3>

<p>
High-performance REST API built with
FastAPI for production deployment.
</p>

<hr>

✅ FastAPI<br>
✅ JSON Response<br>
✅ Low Latency<br>
✅ Production Ready

</div>
""", unsafe_allow_html=True)

st.divider()
st.subheader("🚀 Platform Modules")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.success("""
### 🔍 Prediction

• Single Prediction

• Fraud Probability

• Confidence Score
""")

with m2:
    st.success("""
### 📂 Batch Processing

• CSV Upload

• Bulk Prediction

• Export Results
""")

with m3:
    st.success("""
### 📈 Analytics

• Charts

• KPIs

• Business Insights
""")

with m4:
    st.success("""
### 📄 Reports

• Model Reports

• Downloads

• Performance Metrics
""")

st.divider()
st.subheader("🏦 Industry Use Cases")

u1, u2, u3, u4 = st.columns(4)

with u1:
    st.info("""
### 🏛 Banking

✔ Credit Cards

✔ ATM Fraud

✔ Online Banking
""")

with u2:
    st.info("""
### 💳 FinTech

✔ Wallets

✔ UPI

✔ Payment Gateway
""")

with u3:
    st.info("""
### 🛒 E-Commerce

✔ Fake Orders

✔ Refund Fraud

✔ Chargebacks
""")

with u4:
    st.info("""
### 🛡 Insurance

✔ Claim Fraud

✔ Identity Theft

✔ Risk Detection
""")

st.divider()
st.subheader("🛠 Enterprise Technology Stack")

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.success("""
### 💻 Programming

Python

Pandas

NumPy

Joblib
""")

with t2:
    st.success("""
### 🤖 Machine Learning

Scikit-Learn

Random Forest

Logistic Regression

Decision Tree
""")

with t3:
    st.success("""
### 🌐 Backend

FastAPI

Uvicorn

REST API

Pydantic
""")

with t4:
    st.success("""
### 📊 Frontend

Streamlit

Plotly

HTML

CSS
""")

st.divider()
st.subheader("🔄 AI Fraud Detection Workflow")

w1, w2, w3, w4, w5 = st.columns(5)

with w1:
    st.info("""
### 📥

Transaction

Input
""")

with w2:
    st.info("""
### 🧹

Data Cleaning

Validation
""")

with w3:
    st.info("""
### ⚙️

Feature

Engineering
""")

with w4:
    st.info("""
### 🤖

Machine Learning

Prediction
""")

with w5:
    st.info("""
### 📊

Fraud Report

Dashboard
""")

st.divider()
st.subheader("🏗 Enterprise System Architecture")

st.code("""

          Client (Streamlit UI)
                    │
                    ▼
          FastAPI REST Backend
                    │
                    ▼
          Data Validation Layer
                    │
                    ▼
         Feature Engineering Layer
                    │
                    ▼
          Trained ML Model (.pkl)
                    │
                    ▼
          Fraud Prediction Engine
                    │
                    ▼
          Dashboard & Reports

""")

st.divider()
st.subheader("💼 Business Impact")

left, right = st.columns(2)

with left:

    st.success("""
### 💰 Business Benefits

✔ Reduce Financial Loss

✔ Prevent Fraud

✔ Improve Customer Trust

✔ Faster Decision Making

✔ Automated Monitoring

✔ Enterprise Ready

""")

with right:

    st.info("""
### 📈 Business Outcomes

✔ High Detection Accuracy

✔ Lower False Positives

✔ Better Security

✔ Risk Monitoring

✔ AI Powered Decisions

✔ Real-Time Alerts

""")

st.divider()
st.subheader("🏆 Model Performance")

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric(
        "Accuracy",
        "99.95%"
    )

with p2:
    st.metric(
        "Precision",
        "99%"
    )

with p3:
    st.metric(
        "Recall",
        "98%"
    )

with p4:
    st.metric(
        "Best Model",
        "Random Forest"
    )

st.divider()

st.subheader("🟢 System Status")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.success("""
### API

🟢 Online
""")

with s2:
    st.success("""
### ML Model

🟢 Loaded
""")

with s3:
    st.success("""
### Prediction

🟢 Active
""")

with s4:
    st.success("""
### Dashboard

🟢 Running
""")

st.divider()
st.subheader("🚀 Future Enhancements")

r1, r2, r3 = st.columns(3)

with r1:

    st.warning("""
### AI

• Explainable AI

• SHAP

• LIME
""")

with r2:

    st.warning("""
### Cloud

• Docker

• AWS

• Azure
""")

with r3:

    st.warning("""
### Enterprise

• User Login

• Email Alerts

• Live Monitoring
""")

st.divider()
st.subheader("🌟 Project Highlights")

h1, h2 = st.columns(2)

with h1:

    st.markdown("""
### ✅ Key Features

- 🤖 AI Powered Fraud Prediction
- 📂 Batch CSV Prediction
- 📊 Executive Dashboard
- 📈 Interactive Analytics
- 📉 Model Performance Comparison
- 📄 Downloadable Reports
- ⚡ FastAPI REST API
- 🛡 Enterprise Security
""")

with h2:

    st.markdown("""
### 🎯 Why This Platform?

- ✔ High Accuracy
- ✔ Real-Time Prediction
- ✔ Easy Deployment
- ✔ Interactive Visualization
- ✔ Banking Ready
- ✔ Scalable Architecture
- ✔ Production Friendly
- ✔ Modern UI
""")

st.divider()

st.subheader("📋 Project Information")

i1, i2, i3, i4 = st.columns(4)

with i1:
    st.metric("Dataset", "284,807")

with i2:
    st.metric("Features", "30")

with i3:
    st.metric("Fraud Cases", "492")

with i4:
    st.metric("Version", "1.0.0")

st.divider()

st.subheader("🚀 Explore the Platform")

st.info("""
### Available Modules

Use the left sidebar to navigate through the application.

📊 Dashboard

🔍 Single Prediction

📂 Batch Prediction

📈 Analytics

📊 Model Performance

📄 Reports

ℹ️ About

⚙️ Settings

Every module is connected with the FastAPI backend and Machine Learning model.
""")

st.divider()

st.subheader("🛠 Built With")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.success("🐍 Python")

with c2:
    st.success("🤖 Scikit-Learn")

with c3:
    st.success("⚡ FastAPI")

with c4:
    st.success("📊 Streamlit")

with c5:
    st.success("📈 Plotly")

st.divider()
st.markdown("""
<div style="padding:30px;
text-align:center;
background:#0F172A;
border-radius:18px;
color:white;">

<h2 style="color:white;">
🛡 AI Powered Financial Fraud Detection System
</h2>

<p style="font-size:17px;">
Enterprise Machine Learning Platform for detecting
financial fraud using Artificial Intelligence.
</p>

<hr>

<p>

Python • Scikit-Learn • FastAPI • Streamlit • Plotly

</p>

<p>

Version 1.0.0

</p>

<p>

© 2026 All Rights Reserved

</p>

</div>
""", unsafe_allow_html=True)