import sys
sys.path.append('.')
from theme import apply_theme, page_header, sec_head
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import plotly.express as px

st.set_page_config(page_title="Fraud Detection", page_icon="🚨", layout="wide")
apply_theme()
page_header("🚨", "Fraud Detection", "AI-powered anomaly detection to identify suspicious land transactions.")

@st.cache_data
def generate_transactions():
    np.random.seed(42)
    n = 550

    area = np.concatenate([np.random.randint(500, 10000, 500), np.random.randint(500, 10000, 50)])
    price_per_sqft = np.concatenate([np.random.randint(800, 3000, 500), np.random.randint(10, 100, 50)])
    speed = np.concatenate([np.random.randint(30, 180, 500), np.random.randint(1, 10, 50)])
    prev_owners = np.concatenate([np.random.randint(0, 5, 500), np.random.randint(8, 20, 50)])
    doc_completeness = np.concatenate([np.random.uniform(0.7, 1.0, 500), np.random.uniform(0.1, 0.4, 50)])
    price_deviation = np.concatenate([np.random.uniform(-20, 20, 500), np.random.uniform(-80, -50, 50)])
    is_fraud = [0]*500 + [1]*50

    df = pd.DataFrame({
        'transaction_id': [f'TXN{i:04d}' for i in range(n)],
        'area_sqft': area,
        'price_per_sqft': price_per_sqft,
        'transaction_speed_days': speed,
        'num_previous_owners': prev_owners,
        'document_completeness': doc_completeness,
        'price_deviation_pct': price_deviation,
        'is_fraud': is_fraud
    })

    return df.sample(frac=1, random_state=42).reset_index(drop=True)

@st.cache_resource
def train_fraud_model(df):
    features = ['price_per_sqft', 'transaction_speed_days',
                'num_previous_owners', 'document_completeness',
                'price_deviation_pct']
    X = df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X_scaled)
    return model, scaler, features

df = generate_transactions()
model, scaler, features = train_fraud_model(df)

st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Transactions", len(df))
with col2:
    st.metric("Algorithm", "Isolation Forest")
with col3:
    st.metric("Known Fraud Cases", df['is_fraud'].sum())
with col4:
    st.metric("Detection Method", "Anomaly Detection")

st.markdown("---")

tab1, tab2 = st.tabs(["🔍 Check Transaction", "📊 Transaction Analysis"])

with tab1:
    st.subheader("Enter Transaction Details")

    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("Land Area (sq ft)", min_value=100, max_value=50000, value=1500)
        price = st.number_input("Transaction Price (₹)", min_value=10000, max_value=50000000, value=3000000)
        speed = st.slider("Transaction Speed (days)", 1, 365, 45)

    with col2:
        prev_owners = st.slider("Number of Previous Owners", 0, 20, 2)
        doc_completeness = st.slider("Document Completeness (%)", 0, 100, 85)
        market_price_per_sqft = st.number_input("Market Price per sq ft (₹)", min_value=100, max_value=10000, value=2000)

    price_per_sqft = price / area if area > 0 else 0
    price_deviation = ((price_per_sqft - market_price_per_sqft) / market_price_per_sqft) * 100

    st.info(f"📊 Calculated Price per sq ft: ₹{price_per_sqft:,.0f} | Price Deviation: {price_deviation:.1f}%")

    if st.button("🔍 Check for Fraud", type="primary"):
        input_data = np.array([[price_per_sqft, speed, prev_owners, doc_completeness/100, price_deviation]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        score = model.score_samples(input_scaled)[0]
        fraud_probability = max(0, min(100, (-score - 0.1) * 200))

        st.markdown("---")
        if prediction[0] == -1:
            st.error(f"🚨 SUSPICIOUS TRANSACTION DETECTED! Risk Score: {fraud_probability:.1f}%")
        else:
            st.success(f"✅ Transaction Appears Legitimate. Risk Score: {fraud_probability:.1f}%")

        st.subheader("📋 Risk Factor Analysis")

        checks = [
            (price_deviation < -40, price_deviation < -20, "Price vs Market Value",
             "Price significantly below market", "Price moderately below market", "Price within normal range"),
            (speed < 7, speed < 15, "Transaction Speed",
             "Transaction completed unusually fast", "Transaction speed slightly fast", "Transaction speed normal"),
            (prev_owners > 7, prev_owners > 4, "Ownership History",
             "Too many previous owners", "Above average previous owners", "Normal ownership history"),
            (doc_completeness < 50, doc_completeness < 70, "Document Completeness",
             "Documents very incomplete", "Some documents missing", "Documents complete"),
        ]

        for high_cond, med_cond, label, high_msg, med_msg, low_msg in checks:
            if high_cond:
                st.write(f"🔴 **High Risk** — {high_msg}")
            elif med_cond:
                st.write(f"🟡 **Medium Risk** — {med_msg}")
            else:
                st.write(f"🟢 **Low Risk** — {low_msg}")

with tab2:
    st.subheader("📊 Transaction Dataset Overview")

    scores = model.score_samples(scaler.transform(df[features]))
    df['anomaly_score'] = scores
    df['risk_level'] = pd.cut(scores, bins=3, labels=['High Risk', 'Medium Risk', 'Low Risk'])

    col1, col2 = st.columns(2)

    with col1:
        risk_counts = df['risk_level'].value_counts()
        fig1 = px.pie(values=risk_counts.values, names=risk_counts.index,
                     title="Transaction Risk Distribution",
                     color_discrete_map={'High Risk': 'red', 'Medium Risk': 'orange', 'Low Risk': 'green'})
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.scatter(df, x='price_per_sqft', y='transaction_speed_days',
                         color='risk_level', title="Price vs Transaction Speed",
                         color_discrete_map={'High Risk': 'red', 'Medium Risk': 'orange', 'Low Risk': 'green'})
        st.plotly_chart(fig2, use_container_width=True)