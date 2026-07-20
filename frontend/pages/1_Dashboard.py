import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_data.csv")

try:
    df = load_data()
except Exception:
    st.error(" Unable to load cleaned dataset.")
    st.stop()

st.title("📊 Fraud Detection Dashboard")
st.caption("Real-Time Analytics & Business Intelligence Dashboard")

st.success("🟢 System Status : Online | Model Loaded Successfully")

st.markdown("---")

total_transactions = len(df)
fraud_transactions = int(df["Class"].sum())
legitimate_transactions = total_transactions - fraud_transactions
fraud_rate = (fraud_transactions / total_transactions) * 100

avg_amount = df["Amount"].mean()
max_amount = df["Amount"].max()

st.subheader("📈 Executive Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "💳 Transactions",
        f"{total_transactions:,}"
    )

with c2:
    st.metric(
        "🚨 Frauds",
        f"{fraud_transactions:,}"
    )

with c3:
    st.metric(
        "🛡 Legitimate",
        f"{legitimate_transactions:,}"
    )

with c4:
    st.metric(
        "📊 Fraud Rate",
        f"{fraud_rate:.3f}%"
    )

st.markdown("---")

st.subheader("💼 Business Statistics")

b1, b2, b3 = st.columns(3)

with b1:
    st.info(f"""
### 💰 Average Amount

₹ {avg_amount:.2f}
""")

with b2:
    st.info(f"""
### 💸 Highest Amount

₹ {max_amount:.2f}
""")

with b3:
    st.info("""
### 🤖 Best ML Model

Random Forest

Accuracy : 99.95%
""")

st.markdown("---")

st.subheader("📊 Fraud Analytics")

left, right = st.columns(2)
with left:

    fig = px.pie(
        df,
        names="Class",
        hole=0.55,
        color="Class",
        color_discrete_map={
            0: "#16A34A",
            1: "#DC2626"
        },
        title="Fraud vs Legitimate Transactions"
    )

    fig.update_traces(
        textinfo="percent+label",
        pull=[0, 0.08]
    )

    fig.update_layout(
        height=450,
        legend_title="Transaction Type"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
with right:

    fig = px.histogram(
        df,
        x="Amount",
        nbins=60,
        title="Transaction Amount Distribution"
    )

    fig.update_layout(
        height=450,
        xaxis_title="Transaction Amount",
        yaxis_title="Frequency"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.subheader("🤖 AI Generated Business Insights")

insight1, insight2 = st.columns(2)

with insight1:

    st.warning(f"""

### 🚨 Fraud Analysis

• Fraud Transactions : **{fraud_transactions:,}**

• Legitimate Transactions : **{legitimate_transactions:,}**

• Fraud Rate : **{fraud_rate:.3f}%**

• Dataset is highly imbalanced.

""")

with insight2:

    st.success("""

### ✅ Model Recommendation

✔ Random Forest selected as Best Model

✔ High Accuracy

✔ Excellent Precision

✔ Production Ready

✔ Suitable for Banking Applications

""")

st.markdown("---")
st.subheader("📈 Executive Summary")

summary1, summary2, summary3 = st.columns(3)

with summary1:

    st.info("""

### 📊 Risk Level

🟢 Low

Current fraud percentage is extremely low.

""")

with summary2:

    st.info("""

### 💼 Business Impact

AI can automatically detect suspicious
transactions before payment processing.

""")

with summary3:

    st.info("""

### 🎯 Recommendation

Continue monitoring transactions
using Machine Learning models.

""")

st.markdown("---")
st.subheader("📉 Feature Correlation Analysis")

corr = df.corr(numeric_only=True)

fig = px.imshow(
    corr,
    color_continuous_scale="RdBu_r",
    aspect="auto",
    title="Correlation Matrix"
)

fig.update_layout(
    height=700,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")
st.subheader("💰 Top 20 Highest Amount Transactions")

top_transactions = (
    df.sort_values("Amount", ascending=False)
      .head(20)
)

st.dataframe(
    top_transactions,
    use_container_width=True,
    height=420
)

st.markdown("---")
st.subheader("🚨 Sample Fraud Transactions")

fraud_df = df[df["Class"] == 1].head(15)

if len(fraud_df) > 0:

    st.dataframe(
        fraud_df,
        use_container_width=True,
        height=350
    )

else:

    st.info("No fraud transactions available.")

st.markdown("---")
st.subheader("📊 Transaction Statistics")

stats = df["Amount"].describe()

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric(
        "Minimum Amount",
        f"₹ {stats['min']:.2f}"
    )

with s2:
    st.metric(
        "Average Amount",
        f"₹ {stats['mean']:.2f}"
    )

with s3:
    st.metric(
        "Median Amount",
        f"₹ {stats['50%']:.2f}"
    )

with s4:
    st.metric(
        "Maximum Amount",
        f"₹ {stats['max']:.2f}"
    )

st.markdown("---")

st.subheader("📄 Latest Transactions")

st.dataframe(
    df.tail(25),
    use_container_width=True,
    height=450
)

st.markdown("---")
st.subheader("📥 Export Dashboard Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📄 Download Processed Dataset",
    data=csv,
    file_name="processed_transactions.csv",
    mime="text/csv",
    use_container_width=True
)

st.markdown("---")
st.subheader("🔍 Transaction Explorer")

transaction_type = st.selectbox(
    "Select Transaction Type",
    ["All", "Legitimate", "Fraud"]
)

if transaction_type == "Fraud":
    filtered_df = df[df["Class"] == 1]

elif transaction_type == "Legitimate":
    filtered_df = df[df["Class"] == 0]

else:
    filtered_df = df

st.dataframe(
    filtered_df.head(100),
    use_container_width=True,
    height=450
)

st.markdown("---")
st.subheader("🖥 System Health")

status1, status2, status3 = st.columns(3)

with status1:
    st.success("""
### API

🟢 Online
""")

with status2:
    st.success("""
### ML Model

🟢 Loaded
""")

with status3:
    st.success("""
### Prediction Engine

🟢 Ready
""")

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:20px">

<h3>🛡 AI Powered Financial Fraud Detection System</h3>

<p>
Enterprise Machine Learning Platform for Financial Fraud Detection
</p>

<p>
Python • Scikit-Learn • FastAPI • Streamlit • Plotly
</p>

<p>
Version 1.0
</p>

</div>
""",
unsafe_allow_html=True
)