"""
Single Transaction Prediction
-----------------------------
AI Powered Financial Fraud Detection
"""

import requests
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Single Prediction",
    page_icon="🔍",
    layout="wide"
)

API_URL = API_URL = "https://ai-powered-financial-fraud-detection-6mcp.onrender.com/predict"

st.title("🔍 AI Powered Fraud Prediction")

st.markdown("""
Predict whether a financial transaction is **Fraudulent** or
**Legitimate** using the trained Machine Learning model.
""")

st.divider()

with st.form("prediction_form"):

    st.subheader("Transaction Information")

    col1, col2 = st.columns(2)

    with col1:
        Time = st.number_input(
            "Transaction Time",
            value=0.0
        )

    with col2:
        Amount = st.number_input(
            "Transaction Amount",
            value=0.0,
            min_value=0.0
        )

    st.markdown("### Transaction Features")

    values = {}

    for i in range(1, 29, 2):

        c1, c2 = st.columns(2)

        with c1:

            values[f"V{i}"] = st.number_input(
                f"V{i}",
                value=0.0,
                format="%.6f"
            )

        with c2:

            values[f"V{i+1}"] = st.number_input(
                f"V{i+1}",
                value=0.0,
                format="%.6f"
            )

    submit = st.form_submit_button(
        "🚀 Predict Transaction",
        use_container_width=True
    )

if submit:

    payload = {
        "Time": Time,
        **values,
        "Amount": Amount
    }

    try:

        with st.spinner("Analyzing Transaction..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=10
            )

        if response.status_code != 200:

            st.error("Prediction API returned an error.")

            st.code(response.text)

            st.stop()

        result = response.json()

        prediction = int(result["prediction"])

        probability = float(result["fraud_probability"])

        probability_percent = probability * 100

        st.divider()

        st.header("Prediction Result")


        if prediction == 1:

            st.error("🚨 FRAUD TRANSACTION DETECTED")

            recommendation = "❌ Block this transaction immediately."

        else:

            st.success("✅ LEGITIMATE TRANSACTION")

            recommendation = "✔ Transaction appears safe."


        if probability_percent < 30:

            risk = "🟢 LOW"

        elif probability_percent < 70:

            risk = "🟡 MEDIUM"

        else:

            risk = "🔴 HIGH"


        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Prediction",
                "Fraud" if prediction else "Legitimate"
            )

        with c2:

            st.metric(
                "Fraud Probability",
                f"{probability_percent:.2f}%"
            )

        with c3:

            st.metric(
                "Risk Level",
                risk
            )

        st.divider()


        st.subheader("Fraud Probability Gauge")

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=probability_percent,

            title={"text": "Fraud Probability (%)"},

            gauge={

                "axis": {

                    "range": [0, 100]

                },

                "bar": {

                    "color": "darkred"

                },

                "steps": [

                    {

                        "range": [0, 30],

                        "color": "lightgreen"

                    },

                    {

                        "range": [30, 70],

                        "color": "gold"

                    },

                    {

                        "range": [70, 100],

                        "color": "red"

                    }

                ]

            }

        ))

        fig.update_layout(height=400)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        st.subheader("AI Recommendation")

        if prediction == 1:

            st.error(recommendation)

        else:

            st.success(recommendation)

        st.divider()

        with st.expander("View API Response"):

            st.json(result)

    except requests.exceptions.ConnectionError:

        st.error("""
Unable to connect to FastAPI Backend.

Please start the backend first.

uvicorn backend.api:app --reload
""")

    except requests.exceptions.Timeout:

        st.error("Prediction request timed out.")

    except Exception as e:

        st.error(str(e))