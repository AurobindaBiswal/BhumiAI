# 🏡 BhumiAI — AI Land Intelligence & Legal Verification Platform

> **Developed by Aurobinda Biswal | MTech AI & DS | KIIT University, Bhubaneswar**
> 
> A production-grade multi-agent AI platform for land valuation, legal document verification, fraud detection, and investment advisory using ML, NLP, LLM, RAG, and Multi-Agent Systems.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-bhumai.streamlit.app-red)](https://bhumai.streamlit.app)
[![GitHub](https://img.shields.io/badge/GitHub-BhumiAI-blue)](https://github.com/AurobindaBiswal/BhumiAI)
[![Python](https://img.shields.io/badge/Python-3.14-green)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.58-orange)](https://streamlit.io)

---

## 🚀 Live Demo

👉 **[bhumai.streamlit.app](https://bhumai.streamlit.app)**

Run locally:
```bash
git clone https://github.com/AurobindaBiswal/BhumiAI.git
cd BhumiAI
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Project Overview

BhumiAI is a comprehensive AI-powered platform that solves real-world problems in Indian land transactions. It integrates 13 AI/ML modules into a single unified interface, providing end-to-end intelligence for land buyers, sellers, investors, and legal professionals.

**Resume Line:**
> *"Developed BhumiAI — a multi-agent AI platform for land valuation, legal document intelligence, fraud detection, and investment advisory using RAG, LLMs, NLP, and machine learning. Deployed live on Streamlit Cloud with 13 integrated AI modules."*

---

## 🎯 13 Features

| # | Feature | Technology | Description |
|---|---------|-----------|-------------|
| 1 | 🏠 Land Price Prediction | Random Forest, Scikit-learn | ML model predicts land prices based on location, zone, infrastructure |
| 2 | 📄 Legal Document Analyzer | NLP, PyPDF2, Regex | Upload PDFs, extract parties/amounts/dates, detect red flags |
| 3 | 🚨 Fraud Detection | Isolation Forest, Anomaly Detection | Detect suspicious transactions using unsupervised ML |
| 4 | 📊 Investment Score | Multi-factor Scoring, Plotly | Investment potential across 5 dimensions with radar chart |
| 5 | 🏗️ Development Potential | Rule-based AI, Plotly | Land suitability for Residential/Commercial/Agricultural/Industrial |
| 6 | 🤖 AI Chatbot | LLaMA 3.3 70B, Groq API | Conversational AI for land queries with domain expertise |
| 7 | 📊 Negotiation Strategy | Data-driven Analysis | AI-powered negotiation tactics and price phase analysis |
| 8 | 🔍 RAG Document Q&A | RAG, Keyword Retrieval, LLM | Upload documents and ask questions — answers from document context |
| 9 | 🗺️ Location Map | Plotly Maps, Geospatial | Interactive land price and investment map of Odisha |
| 10 | 📋 PDF Report Generator | ReportLab | Professional downloadable PDF with complete land analysis |
| 11 | 🔍 Advanced RAG | Sentence Transformers, ChromaDB | Semantic search with 384-dim embeddings and cosine similarity |
| 12 | 🤖 Multi-Agent AI | 6 LLM Agents, Groq API | 6 specialized agents collaborate for comprehensive analysis |
| 13 | 🗣️ Voice Assistant | gTTS, LLaMA 3.3 70B | Multilingual voice responses — English, Hindi, Odia |

---

## 🛠️ Technology Stack

### Machine Learning
- **Random Forest** — Land price prediction (1000 training records)
- **Isolation Forest** — Fraud/anomaly detection (550 transactions)
- **Scikit-learn** — ML pipeline and preprocessing
- **XGBoost** — Gradient boosting

### NLP & Generative AI
- **LLaMA 3.3 70B** — Large Language Model via Groq API
- **Sentence Transformers** — Semantic embeddings (384 dimensions)
- **ChromaDB** — Vector database for RAG
- **RAG Pipeline** — Retrieval Augmented Generation
- **Prompt Engineering** — Domain-specific system prompts
- **PyPDF2 + Regex** — Document parsing and NLP
- **gTTS** — Text-to-Speech (EN/HI/OD)

### Multi-Agent System
```
Agent 1: Land Valuation Agent      → Price analysis
Agent 2: Legal Verification Agent  → Document verification  
Agent 3: Fraud Detection Agent     → Risk assessment
Agent 4: Development Analysis      → Development potential
Agent 5: Investment Advisory       → Investment recommendation
Agent 6: Report Generation         → Final comprehensive report
```

### Data & Visualization
- **Pandas & NumPy** — Data processing
- **Plotly** — Interactive charts, radar charts, geospatial maps
- **Streamlit** — Full-stack web interface
- **ReportLab** — PDF generation

### DevOps & Deployment
- **Git & GitHub** — Version control
- **Streamlit Cloud** — Cloud deployment
- **Streamlit Secrets** — Secure API key management

---

## 🏗️ System Architecture

```
BhumiAI Platform
│
├── 🔵 Traditional ML Layer
│   ├── Random Forest (Price Prediction)
│   └── Isolation Forest (Fraud Detection)
│
├── 🟢 NLP Layer  
│   ├── Regex + PyPDF2 (Document Parsing)
│   └── Rule-based Analysis
│
├── 🔴 GenAI Layer
│   ├── Basic RAG (Keyword Search)
│   ├── Advanced RAG (Semantic Search)
│   │   ├── Sentence Transformers → 384-dim embeddings
│   │   ├── ChromaDB Vector Database
│   │   └── Cosine Similarity Search
│   └── Multi-Agent System (6 LLM Agents)
│
└── 🟡 Interface Layer
    ├── Streamlit Web App
    ├── PDF Report Generator
    └── Voice Assistant (EN/HI/OD)
```

---

## 📁 Project Structure

```
BhumiAI/
│
├── app.py                              # Main homepage
├── requirements.txt                    # Dependencies
├── pages/
│   ├── 1_Land_Price_Prediction.py     # ML price prediction
│   ├── 2_Legal_Document_Analyzer.py   # NLP document analysis
│   ├── 3_Fraud_Detection.py           # Anomaly detection
│   ├── 4_Investment_Score.py          # Investment scoring
│   ├── 5_Development_Potential.py     # Development analysis
│   ├── 6_AI_Chatbot.py               # LLM chatbot
│   ├── 7_Negotiation_Strategy.py      # Negotiation AI
│   ├── 8_RAG_Document_QA.py          # Basic RAG Q&A
│   ├── 9_Location_Map.py             # Geospatial map
│   ├── 10_PDF_Report_Generator.py    # PDF reports
│   ├── 11_Advanced_RAG.py            # Semantic RAG
│   ├── 12_Multi_Agent_AI.py          # Multi-agent system
│   └── 13_Voice_Assistant.py         # Voice interface
│
├── data/                              # Data directory
├── models/                            # Saved models
└── README.md
```

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/AurobindaBiswal/BhumiAI.git
cd BhumiAI

# Install dependencies
pip install streamlit pandas numpy scikit-learn xgboost PyPDF2 plotly groq
pip install python-multipart reportlab chromadb sentence-transformers
pip install SpeechRecognition gtts pydub

# Add Groq API Key
# Get free key at: https://console.groq.com

# Run
streamlit run app.py
```

---

## 📊 Datasets

| Dataset | Records | Purpose |
|---|---|---|
| Synthetic Land Data | 1,000 | Price prediction training |
| Transaction Data | 550 | Fraud detection (500 normal + 50 fraudulent) |
| Odisha Location Data | 26 locations | Map visualization |

---

## 🗺️ Odisha Focus

- Bhubaneswar, Cuttack, Puri, Rourkela, Sambalpur mapped
- Odisha-specific documents: Bhulekh, RoR, Patta
- KIIT University area pricing included
- Local stamp duty rates (5%) and registration fees (1%)
- Voice support for Odia language

---

## 👨‍💻 Developer

**Aurobinda Biswal**
MTech — Artificial Intelligence & Data Science
KIIT University, Bhubaneswar, Odisha
Personal AI Project — 2026

---

## ⭐ If you found this helpful, give it a star!
