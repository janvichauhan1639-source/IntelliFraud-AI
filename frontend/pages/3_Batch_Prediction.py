"""
Batch Prediction
----------------
Predict Fraud for Multiple Transactions
"""

import requests
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/predict"

st.title("📂 Batch Fraud Prediction")

st.markdown("""
Upload a CSV file containing multiple transactions.

The AI model will predict whether each transaction is
**Fraudulent** or **Legitimate**.
""")

st.divider()

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

    except Exception as e:

        st.error(str(e))
        st.stop()

    st.subheader("Uploaded Dataset")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    st.info(f"Total Transactions : {len(df):,}")

    st.divider()

    if st.button(
        "🚀 Predict All Transactions",
        use_container_width=True
    ):

        predictions = []
        probabilities = []

        progress = st.progress(0)

        status = st.empty()

        total_rows = len(df)

        try:

            for index, row in enumerate(df.to_dict(orient="records")):

                response = requests.post(
                    API_URL,
                    json=row,
                    timeout=10
                )

                if response.status_code != 200:

                    st.error(
                        f"Prediction failed at row {index+1}"
                    )

                    st.stop()

                result = response.json()

                prediction = int(result["prediction"])

                probability = float(
                    result["fraud_probability"]
                )

                predictions.append(prediction)

                probabilities.append(
                    round(probability * 100, 2)
                )

                progress.progress(
                    (index + 1) / total_rows
                )

                status.text(
                    f"Processing {index+1}/{total_rows}"
                )

            df["Prediction"] = predictions

            df["Label"] = [
                "Fraud"
                if x == 1
                else "Legitimate"
                for x in predictions
            ]

            df["Fraud Probability (%)"] = probabilities

            st.success("Prediction Completed Successfully")

            st.divider()

            c1, c2, c3 = st.columns(3)

            fraud_count = sum(predictions)

            legit_count = len(predictions) - fraud_count

            with c1:

                st.metric(
                    "Total Transactions",
                    len(predictions)
                )

            with c2:

                st.metric(
                    "Fraud Transactions",
                    fraud_count
                )

            with c3:

                st.metric(
                    "Legitimate",
                    legit_count
                )

            st.divider()

            st.subheader("Prediction Results")

            st.dataframe(
                df,
                use_container_width=True,
                height=500
            )

            csv = df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(

                "📥 Download Results",

                data=csv,

                file_name="batch_prediction_results.csv",

                mime="text/csv",

                use_container_width=True

            )

        except requests.exceptions.ConnectionError:

            st.error("""
Unable to connect to FastAPI Backend.

Please run:

uvicorn backend.api:app --reload
""")

        except Exception as e:

            st.error(str(e))

else:

    st.info("Please upload a CSV file to begin.")