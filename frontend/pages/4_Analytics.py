"""
Analytics Page
--------------
Advanced Data Analytics
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
from pandas.errors import EmptyDataError

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)


@st.cache_data
def load_data():

    base = Path(__file__).resolve().parents[2]

    possible_files = [
        base / "data" / "processed" / "train.csv",
        base / "data" / "processed" / "cleaned_data.csv",
    ]

    for file in possible_files:

        if file.exists():

            try:
                df = pd.read_csv(file)

                if df.empty:
                    continue

                return df

            except EmptyDataError:
                continue

    st.error("""
❌ Dataset not available.

Please generate the processed dataset first.

Run:

python run.py
""")

    st.stop()


df = load_data()

st.title("📈 Advanced Fraud Analytics")

st.markdown("""
Explore transaction patterns,
fraud distribution,
feature relationships,
and business insights.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    selected_class = st.selectbox(
        "Transaction Type",
        ["All", "Legitimate", "Fraud"]
    )

with col2:

    max_amount = st.slider(
        "Maximum Amount",
        float(df["Amount"].min()),
        float(df["Amount"].max()),
        float(df["Amount"].max())
    )

filtered_df = df[df["Amount"] <= max_amount]

if selected_class == "Fraud":

    filtered_df = filtered_df[
        filtered_df["Class"] == 1
    ]

elif selected_class == "Legitimate":

    filtered_df = filtered_df[
        filtered_df["Class"] == 0
    ]

st.divider()

c1, c2, c3 = st.columns(3)

c1.metric(
    "Transactions",
    len(filtered_df)
)

c2.metric(
    "Frauds",
    int(filtered_df["Class"].sum())
)

c3.metric(
    "Average Amount",
    f"₹ {filtered_df['Amount'].mean():.2f}"
)

st.divider()

left, right = st.columns(2)

with left:

    fig = px.pie(
        filtered_df,
        names="Class",
        hole=0.45,
        title="Transaction Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.histogram(
        filtered_df,
        x="Amount",
        nbins=60,
        title="Transaction Amount Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

sample = filtered_df.sample(
    min(len(filtered_df), 5000),
    random_state=42
)

left, right = st.columns(2)

with left:

    fig = px.scatter(
        sample,
        x="Time",
        y="Amount",
        color="Class",
        title="Time vs Amount"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.box(
        filtered_df,
        x="Class",
        y="Amount",
        title="Amount by Transaction Class"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

st.subheader("Correlation Heatmap")

corr = filtered_df.corr(numeric_only=True)

fig = px.imshow(
    corr,
    aspect="auto",
    color_continuous_scale="RdBu_r"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("Top 20 Highest Transactions")

top_df = filtered_df.sort_values(
    "Amount",
    ascending=False
).head(20)

st.dataframe(
    top_df,
    use_container_width=True
)

st.divider()

st.subheader("Business Insights")

frauds = int(filtered_df["Class"].sum())

total = len(filtered_df)

avg_amount = filtered_df["Amount"].mean()

max_amount = filtered_df["Amount"].max()

st.success(f"""
### Key Insights

- Total Transactions : **{total:,}**
- Fraud Transactions : **{frauds:,}**
- Average Amount : **₹ {avg_amount:.2f}**
- Maximum Amount : **₹ {max_amount:.2f}**
- Dataset is highly imbalanced, therefore fraud-aware models such as Random Forest and XGBoost are appropriate.
""")