"""
Analytics Page
--------------
Advanced Data Analytics
"""

from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)


@st.cache_data
def load_data():
    base_path = Path(__file__).resolve().parents[2]
    data_path = base_path / "data" / "processed" / "train.csv"

    if not data_path.exists():
        st.error(f"Dataset not found:\n{data_path}")
        st.stop()

    return pd.read_csv(data_path)


df = load_data()

st.title("📈 Advanced Fraud Analytics")

st.markdown("""
Explore transaction patterns, fraud distribution,
feature relationships and business insights.
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
    filtered_df = filtered_df[filtered_df["Class"] == 1]

elif selected_class == "Legitimate":
    filtered_df = filtered_df[filtered_df["Class"] == 0]

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Transactions",
        len(filtered_df)
    )

with c2:
    st.metric(
        "Frauds",
        int(filtered_df["Class"].sum())
    )

with c3:
    st.metric(
        "Average Amount",
        f"₹ {filtered_df['Amount'].mean():.2f}"
    )

st.divider()

left, right = st.columns(2)

with left:
    fig = px.pie(
        filtered_df,
        names="Class",
        hole=0.5,
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
        title="Amount Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

left, right = st.columns(2)

with left:
    sample = filtered_df.sample(
        min(5000, len(filtered_df)),
        random_state=42
    )

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
        title="Amount by Class"
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
    color_continuous_scale="RdBu_r",
    aspect="auto"
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

st.success(f"""
### Key Observations

• Total Transactions: {len(filtered_df):,}

• Fraud Cases: {int(filtered_df['Class'].sum())}

• Average Amount: ₹ {filtered_df['Amount'].mean():.2f}

• Maximum Amount: ₹ {filtered_df['Amount'].max():.2f}

• Dataset is highly imbalanced and requires fraud-aware models.
""")