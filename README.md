# 🏡 BhumiAI — AI Land Intelligence & Legal Verification Platform

> **MTech AI & DS Final Year Project**  
> An intelligent multi-agent platform for land valuation, legal document verification, fraud detection, and investment advisory using ML, NLP, LLM, and RAG.

---

## 🚀 Live Demo

Run locally using Streamlit:
```bash
streamlit run app.py
```

---

## 📌 Project Overview

BhumiAI is a comprehensive AI-powered platform that solves real-world problems in Indian land transactions. It integrates multiple AI/ML technologies into a single unified interface, providing end-to-end intelligence for land buyers, sellers, investors, and legal professionals.

**Resume Line:**
> *Developed a multi-agent AI platform for land valuation, legal document intelligence, fraud detection, and investment advisory using RAG, LLMs, NLP, and machine learning.*

---

## 🎯 Features

| # | Feature | Technology | Description |
|---|---------|-----------|-------------|
| 1 | 🏠 Land Price Prediction | Random Forest, Scikit-learn | Predict land prices based on location, zone, infrastructure factors |
| 2 | 📄 Legal Document Analyzer | NLP, PyPDF2, Regex | Upload PDFs, extract parties/amounts/dates, detect red flags |
| 3 | 🚨 Fraud Detection | Isolation Forest, Anomaly Detection | Detect suspicious land transactions using unsupervised ML |
| 4 | 📊 Investment Score | Multi-factor Scoring, Plotly | Calculate investment potential across 5 dimensions |
| 5 | 🏗️ Development Potential | Rule-based AI, Plotly | Analyze land suitability for Residential/Commercial/Industrial use |
| 6 | 🤖 AI Chatbot | LLaMA 3.3 70B, Groq API, Prompt Engineering | Conversational AI for land-related queries |
| 7 | 📊 Negotiation Strategy | Data-driven Analysis | AI-powered negotiation tactics and price phase analysis |
| 8 | 🔍 RAG Document Q&A | RAG, LLM, Chunking | Upload documents and ask questions — AI answers from document context |
| 9 | 🗺️ Location Map | Plotly Maps, Geospatial | Visual land price and investment map of Odisha |

---

## 🛠️ Technology Stack

### Machine Learning
- **Random Forest** — Land price prediction
- **Isolation Forest** — Fraud/anomaly detection
- **Scikit-learn** — ML pipeline
- **XGBoost** — Gradient boosting

### NLP & Generative AI
- **LLaMA 3.3 70B** — Large Language Model via Groq API
- **RAG (Retrieval Augmented Generation)** — Document Q&A
- **Prompt Engineering** — Domain-specific system prompts
- **PyPDF2 + Regex** — Document parsing and NLP

### Data & Visualization
- **Pandas & NumPy** — Data processing
- **Plotly** — Interactive charts, radar charts, maps
- **Streamlit** — Full-stack web interface

### Concepts Implemented
- Multi-Agent AI Architecture
- Anomaly Detection
- RAG Pipeline
- Synthetic Data Generation
- Geospatial Visualization

---

## 📁 Project Structure

```
BhumiAI/
│
├── app.py                          # Main homepage
├── pages/
│   ├── 1_Land_Price_Prediction.py  # ML price prediction
│   ├── 2_Legal_Document_Analyzer.py # NLP document analysis
│   ├── 3_Fraud_Detection.py        # Anomaly detection
│   ├── 4_Investment_Score.py       # Investment scoring
│   ├── 5_Development_Potential.py  # Development analysis
│   ├── 6_AI_Chatbot.py             # LLM chatbot
│   ├── 7_Negotiation_Strategy.py   # Negotiation AI
│   ├── 8_RAG_Document_QA.py        # RAG Q&A system
│   └── 9_Location_Map.py           # Geospatial map
│
├── data/                           # Data directory
├── models/                         # Saved models
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/AurobindaBiswal/BhumiAI.git
cd BhumiAI
```

### 2. Install dependencies
```bash
pip install streamlit pandas numpy scikit-learn xgboost PyPDF2 plotly groq python-multipart fastapi uvicorn
```

### 3. Add Groq API Key
In `pages/6_AI_Chatbot.py` and `pages/8_RAG_Document_QA.py`:
```python
GROQ_API_KEY = "your_groq_api_key_here"
```
Get your free API key at: https://console.groq.com

### 4. Run the app
```bash
streamlit run app.py
```

Open browser at: `http://localhost:8501`

---

## 🧠 How It Works

### Land Price Prediction
1. Synthetic Indian land dataset generated (1000 records)
2. Features: area, location, zone, infrastructure ratings
3. Random Forest model trained with 100 estimators
4. R² Score: ~1.0 on synthetic data

### Fraud Detection
1. 550 transactions (500 normal + 50 fraudulent) generated
2. Isolation Forest detects anomalies without labeled data
3. Risk factors analyzed: price deviation, transaction speed, ownership history

### RAG System
1. Document uploaded and split into chunks (2000 chars with 200 overlap)
2. Relevant chunks retrieved using keyword matching
3. LLaMA 3.3 70B generates answers based on retrieved context

### Legal Document Analyzer
1. PDF text extracted using PyPDF2
2. Regex patterns detect dates, amounts, parties, plot numbers
3. Keyword matching for compliance checks and red flags

---

## 📊 Dataset

All datasets are synthetically generated to simulate Indian land market conditions:
- **Land Price Dataset:** 1000 records across 10 Indian states
- **Transaction Dataset:** 550 records (500 normal, 50 fraudulent)
- **Location Dataset:** 26 locations across Odisha

---

## 🗺️ Odisha Focus

The platform has special focus on Odisha:
- Bhubaneswar, Cuttack, Puri, Rourkela, Sambalpur mapped
- Odisha-specific legal documents (Bhulekh, RoR, Patta)
- Local land laws and stamp duty rates included
- KIIT University area pricing included

---

👨‍💻 Developer
Aurobinda Biswal
MTech — Artificial Intelligence & Data Science
KIIT University, Bhubaneswar, Odisha
Built as a personal AI project — 2026

---

## 📄 License

This project is developed for academic purposes as an MTech Final Year Project.

---

## ⭐ If you found this helpful, give it a star!
