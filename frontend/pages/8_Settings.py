"""
Settings Page
-------------
Application Configuration & System Status
"""

import streamlit as st
import requests

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Application Settings")

st.markdown(
    "Manage application configuration and monitor backend health."
)

st.divider()

st.subheader("🖥 Backend Status")

backend_url = "http://127.0.0.1:8000"

try:

    response = requests.get(
        f"{backend_url}/health",
        timeout=5
    )

    if response.status_code == 200:

        health = response.json()

        st.success("🟢 FastAPI Backend is Online")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Backend",
                health.get("backend", "Online")
            )

        with col2:
            st.metric(
                "Status",
                health.get("status", "Healthy")
            )

        with col3:
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

st.subheader("📡 API Information")

try:

    info = requests.get(
        f"{backend_url}/info",
        timeout=5
    )

    if info.status_code == 200:

        data = info.json()

        c1, c2 = st.columns(2)

        with c1:

            st.info(f"""
### 📦 Project

{data.get("project")}

### 🌐 Framework

{data.get("framework")}

### 🤖 Machine Learning

{data.get("machine_learning")}
""")

        with c2:

            st.info(f"""
### 💻 Frontend

{data.get("frontend")}

### 🏆 Best Model

{data.get("best_model")}
""")

except:
    st.warning("API information unavailable.")

st.divider()

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


st.subheader("💻 System Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### Backend

✅ FastAPI

REST API

Online
""")

with col2:
    st.success("""
### AI Model

✅ Random Forest

Loaded

Ready
""")

with col3:
    st.success("""
### Frontend

✅ Streamlit

Interactive

Running
""")

st.divider()

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