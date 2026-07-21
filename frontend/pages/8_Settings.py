"""
Settings Page
-------------
Application Configuration & System Status
"""

import os
import streamlit as st
import requests

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

# Backend URL
backend_url = os.getenv(
    "BACKEND_URL",
    "https://ai-powered-financial-fraud-detection-6mcp.onrender.com"
)

st.title("⚙️ Application Settings")

st.markdown(
    "Manage application configuration and monitor backend health."
)

st.divider()

# ----------------------------------------------------
# Backend Status
# ----------------------------------------------------

st.subheader("🖥 Backend Status")

try:

    response = requests.get(
        f"{backend_url}/health",
        timeout=10
    )

    if response.status_code == 200:

        health = response.json()

        st.success("🟢 FastAPI Backend is Online")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Backend",
                health.get("backend", "Online")
            )

        with c2:
            st.metric(
                "Status",
                health.get("status", "Healthy")
            )

        with c3:
            st.metric(
                "Model",
                health.get("model", "Loaded")
            )

    else:

        st.error(
            f"Backend returned status code {response.status_code}"
        )

except Exception as e:

    st.error("🔴 Backend is Offline")
    st.caption(str(e))

st.divider()

# ----------------------------------------------------
# API Information
# ----------------------------------------------------

st.subheader("📡 API Information")

try:

    response = requests.get(
        f"{backend_url}/",
        timeout=10
    )

    if response.status_code == 200:

        data = response.json()

        c1, c2 = st.columns(2)

        with c1:

            st.info(f"""
### 📦 Project

AI Powered Financial Fraud Detection System

### 🌐 Framework

FastAPI

### 🤖 Machine Learning

Scikit-Learn
""")

        with c2:

            st.info(f"""
### 💻 Frontend

Streamlit

### 🏆 Version

{data.get("version","1.0.0")}
""")

    else:

        st.warning("API information unavailable.")

except Exception:

    st.warning("API information unavailable.")

st.divider()

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

st.subheader("⚙️ Configuration")

st.text_input(
    "Backend URL",
    value=backend_url,
    disabled=True
)

st.text_input(
    "Best Model",
    value="Random Forest",
    disabled=True
)

st.text_input(
    "Frontend",
    value="Streamlit",
    disabled=True
)

st.text_input(
    "Backend Framework",
    value="FastAPI",
    disabled=True
)

st.text_input(
    "Machine Learning",
    value="Scikit-Learn",
    disabled=True
)

st.text_input(
    "Dataset",
    value="Credit Card Fraud Detection",
    disabled=True
)

st.divider()

# ----------------------------------------------------
# System Information
# ----------------------------------------------------

st.subheader("💻 System Information")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("""
### Backend

✅ FastAPI

REST API

Online
""")

with c2:

    st.success("""
### AI Model

✅ Random Forest

Loaded

Ready
""")

with c3:

    st.success("""
### Frontend

✅ Streamlit

Interactive

Running
""")

st.divider()

# ----------------------------------------------------
# Refresh
# ----------------------------------------------------

st.subheader("🔄 Actions")

if st.button(
    "Refresh Backend Status",
    use_container_width=True
):
    st.rerun()

st.divider()

st.markdown(
"""
<div style="text-align:center;padding:20px">

<h3>⚙️ AI Powered Financial Fraud Detection System</h3>

<p>
Enterprise Machine Learning Platform
</p>

<p>
Python • FastAPI • Streamlit • Scikit-Learn
</p>

<p>
Version 1.0.0
</p>

</div>
""",
unsafe_allow_html=True
)