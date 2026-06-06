import streamlit as st

st.set_page_config(
    page_title="AI Land Intelligence Platform",
    page_icon="🏡",
    layout="wide"
)

# Header
st.title("🏡 AI Land Intelligence & Legal Verification Platform")
st.subheader("MTech AI & DS Final Year Project")
st.markdown("*An intelligent platform for land valuation, legal verification, fraud detection, and investment advisory using ML, NLP, LLM, and RAG.*")

st.markdown("---")

# Stats row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("ML Models", "3", "Trained")
with col2:
    st.metric("AI Features", "6", "Modules")
with col3:
    st.metric("Technologies", "7+", "ML/DL/NLP/LLM")
with col4:
    st.metric("Data Points", "1550+", "Transactions")

st.markdown("---")

# Features
st.subheader("🚀 Platform Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("### 🏠 Land Price Prediction")
    st.write("""
    Predict land prices across Indian states using **Random Forest ML model** 
    trained on synthetic Indian land data.
    
    **Technologies:** Scikit-learn, Random Forest, Pandas, NumPy
    """)
    st.page_link("pages/1_Land_Price_Prediction.py", label="Open Feature →")

with col2:
    st.info("### 📄 Legal Document Analyzer")
    st.write("""
    Upload land legal documents (PDF) for automated analysis, 
    compliance checking, and red flag detection using **NLP & Regex**.
    
    **Technologies:** PyPDF2, NLP, Regular Expressions
    """)
    st.page_link("pages/2_Legal_Document_Analyzer.py", label="Open Feature →")

with col3:
    st.warning("### 🚨 Fraud Detection")
    st.write("""
    Detect suspicious land transactions using **Isolation Forest** 
    anomaly detection algorithm on transaction patterns.
    
    **Technologies:** Isolation Forest, Scikit-learn, Plotly
    """)
    st.page_link("pages/3_Fraud_Detection.py", label="Open Feature →")

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.success("### 📊 Investment Score")
    st.write("""
    Calculate comprehensive investment scores using **weighted 
    multi-factor scoring model** across location, legal, market, 
    infrastructure and risk parameters.
    
    **Technologies:** Custom Scoring Algorithm, Plotly Radar Chart
    """)
    st.page_link("pages/4_Investment_Score.py", label="Open Feature →")

with col5:
    st.info("### 🏗️ Development Potential")
    st.write("""
    Analyze land development suitability for Residential, Commercial, 
    Agricultural, and Industrial use with **ROI estimation**.
    
    **Technologies:** Rule-based AI, Plotly, Pandas
    """)
    st.page_link("pages/5_Development_Potential.py", label="Open Feature →")

with col6:
    st.warning("### 🤖 AI Chatbot")
    st.write("""
    Conversational AI assistant for land queries powered by 
    **LLaMA 3.3 70B** via Groq API with domain-specific system prompting.
    
    **Technologies:** LLM, Groq API, LLaMA 3.3, Prompt Engineering
    """)
    st.page_link("pages/6_AI_Chatbot.py", label="Open Feature →")

st.markdown("---")

# Tech stack
st.subheader("🛠️ Technology Stack")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.info("**Machine Learning**\nRandom Forest\nIsolation Forest\nScikit-learn\nXGBoost")
with col2:
    st.info("**NLP & AI**\nNLP & Regex\nLLaMA 3.3 70B\nGroq API\nPrompt Engineering")
with col3:
    st.info("**Data & Viz**\nPandas & NumPy\nPlotly\nStreamlit\nPyPDF2")
with col4:
    st.info("**Concepts**\nAnomaly Detection\nRAG Architecture\nMulti-Agent AI\nSynthetic Data")

st.markdown("---")
st.caption("Developed by MTech AI & DS Student | AI Land Intelligence Platform © 2024")