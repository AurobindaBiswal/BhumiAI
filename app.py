import streamlit as st

st.set_page_config(
    page_title="BhumiAI — Land Intelligence Platform",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    .stApp {
        background: linear-gradient(135deg, #0d0015 0%, #1a0030 30%, #0d0020 60%, #1a0a00 100%);
        min-height: 100vh;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: 
            radial-gradient(ellipse at 20% 50%, rgba(120,0,255,0.15) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 20%, rgba(255,180,0,0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 80%, rgba(180,0,255,0.1) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }

    .hero {
        text-align: center;
        padding: 4rem 2rem 3rem;
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(180,100,255,0.2);
        border-radius: 30px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(120,0,255,0.2), inset 0 1px 0 rgba(255,255,255,0.1);
    }

    .logo-text {
        font-size: 5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #c084fc 0%, #fbbf24 40%, #f59e0b 60%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -2px;
        line-height: 1;
        margin-bottom: 0.5rem;
        filter: drop-shadow(0 0 30px rgba(168,85,247,0.5));
    }

    .logo-icon {
        font-size: 4rem;
        margin-bottom: 0.5rem;
        display: block;
        filter: drop-shadow(0 0 20px rgba(251,191,36,0.8));
    }

    .hero-tagline {
        font-size: 1.3rem;
        font-weight: 600;
        color: #e9d5ff;
        margin-bottom: 0.8rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero-desc {
        font-size: 1rem;
        color: #c4b5fd;
        max-width: 650px;
        margin: 0 auto 1.5rem;
        line-height: 1.7;
    }

    .live-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: linear-gradient(135deg, rgba(34,197,94,0.2), rgba(16,185,129,0.1));
        border: 1px solid rgba(34,197,94,0.4);
        border-radius: 50px;
        padding: 0.4rem 1.2rem;
        font-size: 0.85rem;
        color: #4ade80;
        font-weight: 600;
        letter-spacing: 1px;
        backdrop-filter: blur(10px);
    }

    .live-dot {
        width: 8px; height: 8px;
        background: #4ade80;
        border-radius: 50%;
        animation: livePulse 1.5s infinite;
        display: inline-block;
    }

    @keyframes livePulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.2); }
    }

    .stat-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(180,100,255,0.3);
        border-radius: 20px;
        padding: 1.8rem 1rem;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(120,0,255,0.15);
    }

    .stat-card:hover {
        transform: translateY(-5px);
        border-color: rgba(251,191,36,0.6);
        box-shadow: 0 12px 40px rgba(251,191,36,0.25);
    }

    .stat-number {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }

    .stat-label {
        font-size: 0.8rem;
        color: #e9d5ff;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 0.5rem;
    }

    .feat-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(168,85,247,0.25);
        border-radius: 20px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(120,0,255,0.1);
        margin-bottom: 0.5rem;
        min-height: 200px;
    }

    .feat-card:hover {
        border-color: rgba(251,191,36,0.5);
        transform: translateY(-4px);
        box-shadow: 0 15px 40px rgba(251,191,36,0.2);
    }

    .feat-emoji {
        font-size: 2.2rem;
        margin-bottom: 0.8rem;
        display: block;
        filter: drop-shadow(0 0 10px rgba(251,191,36,0.6));
    }

    .feat-name {
        font-size: 1.05rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }

    .feat-desc {
        font-size: 0.82rem;
        color: #d8b4fe;
        line-height: 1.6;
        margin-bottom: 0.8rem;
    }

    .feat-tech {
        font-size: 0.72rem;
        color: #fbbf24;
        font-weight: 700;
        background: rgba(251,191,36,0.1);
        border: 1px solid rgba(251,191,36,0.3);
        border-radius: 8px;
        padding: 0.3rem 0.7rem;
        display: inline-block;
    }

    .sec-title {
        font-size: 1.6rem;
        font-weight: 800;
        color: #ffffff;
        margin: 2rem 0 1.2rem;
        padding-left: 1rem;
        border-left: 4px solid #fbbf24;
    }

    .badge {
        display: inline-block;
        background: rgba(168,85,247,0.2);
        border: 1px solid rgba(168,85,247,0.4);
        border-radius: 30px;
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        color: #e9d5ff;
        margin: 0.2rem;
        font-weight: 600;
    }

    .arch-card {
        background: rgba(255,255,255,0.04);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(168,85,247,0.25);
        border-radius: 20px;
        padding: 1.5rem;
    }

    .footer {
        text-align: center;
        padding: 2.5rem 1rem;
        margin-top: 3rem;
        border-top: 1px solid rgba(168,85,247,0.3);
        color: #a78bfa;
        font-size: 0.85rem;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: rgba(13,0,21,0.97) !important;
        border-right: 1px solid rgba(168,85,247,0.3) !important;
    }

    section[data-testid="stSidebar"] * {
        color: #e9d5ff !important;
        font-weight: 600 !important;
    }

    section[data-testid="stSidebar"] a {
        color: #fbbf24 !important;
        font-weight: 700 !important;
    }

    /* PAGE LINKS — BRIGHT & VISIBLE */
    a[data-testid="stPageLink-NavLink"] {
        color: #fbbf24 !important;
        font-weight: 700 !important;
        font-size: 0.88rem !important;
        opacity: 1 !important;
        border: 1px solid rgba(251,191,36,0.4) !important;
        border-radius: 10px !important;
        padding: 0.4rem 1rem !important;
        display: inline-block !important;
        margin-top: 0.8rem !important;
        background: rgba(251,191,36,0.1) !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
        text-align: center !important;
    }

    a[data-testid="stPageLink-NavLink"]:hover {
        background: rgba(251,191,36,0.25) !important;
        border-color: #fbbf24 !important;
        transform: scale(1.02) !important;
    }

    a[data-testid="stPageLink-NavLink"] p {
        color: #fbbf24 !important;
        font-weight: 700 !important;
    }
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <span class="logo-icon">🏡</span>
    <div class="logo-text">BhumiAI</div>
    <div class="hero-tagline">AI Land Intelligence & Legal Verification Platform</div>
    <div class="hero-desc">
        A production-grade multi-agent AI platform for land valuation, legal document verification, 
        fraud detection, and investment advisory — powered by ML, NLP, LLM, RAG & Multi-Agent Systems.
    </div>
    <div>
        <span class="live-pill">
            <span class="live-dot"></span>
            LIVE ON STREAMLIT CLOUD
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# STATS
st.markdown('<div class="sec-title">📊 Platform Stats</div>', unsafe_allow_html=True)
stats = [("13", "AI FEATURES"), ("3", "ML MODELS"), ("6", "AI AGENTS"), ("1550+", "DATA POINTS"), ("3", "LANGUAGES"), ("1", "LIVE DEPLOY")]
cols = st.columns(6)
for col, (num, label) in zip(cols, stats):
    with col:
        st.markdown(f'<div class="stat-card"><div class="stat-number">{num}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)

# FEATURES
st.markdown('<div class="sec-title">🚀 Platform Features</div>', unsafe_allow_html=True)

features = [
    ("🏠", "Land Price Prediction", "Predict land prices using Random Forest ML trained on Indian land data.", "Random Forest • Scikit-learn", "pages/1_Land_Price_Prediction.py"),
    ("📄", "Legal Document Analyzer", "Upload PDFs — extract parties, amounts, dates and detect red flags.", "NLP • PyPDF2 • Regex", "pages/2_Legal_Document_Analyzer.py"),
    ("🚨", "Fraud Detection", "Detect suspicious transactions using Isolation Forest anomaly detection.", "Isolation Forest • Unsupervised ML", "pages/3_Fraud_Detection.py"),
    ("📊", "Investment Score", "5-dimension investment scoring with interactive radar chart.", "Multi-factor • Plotly Radar", "pages/4_Investment_Score.py"),
    ("🏗️", "Development Potential", "Analyze land suitability for Residential, Commercial, Agricultural use.", "Rule-based AI • ROI Estimation", "pages/5_Development_Potential.py"),
    ("🤖", "AI Chatbot", "Conversational AI for land queries powered by LLaMA 3.3 70B.", "LLaMA 3.3 70B • Groq API", "pages/6_AI_Chatbot.py"),
    ("💰", "Negotiation Strategy", "AI-powered negotiation tactics with price phase analysis.", "Data-driven • Price Modeling", "pages/7_Negotiation_Strategy.py"),
    ("🔍", "RAG Document Q&A", "Upload documents, ask questions — AI answers from your document.", "RAG • Keyword Retrieval • LLM", "pages/8_RAG_Document_QA.py"),
    ("🗺️", "Location Map", "Interactive land price and investment map of Odisha.", "Plotly Maps • Geospatial", "pages/9_Location_Map.py"),
    ("📋", "PDF Report Generator", "Generate professional downloadable PDF land analysis reports.", "ReportLab • Auto-generation", "pages/10_PDF_Report_Generator.py"),
    ("🧠", "Advanced RAG", "Semantic search with Sentence Transformers + ChromaDB vectors.", "Sentence Transformers • ChromaDB", "pages/11_Advanced_RAG.py"),
    ("🤝", "Multi-Agent AI", "6 specialized AI agents collaborate for comprehensive analysis.", "6 LLM Agents • Orchestration", "pages/12_Multi_Agent_AI.py"),
    ("🗣️", "Voice Assistant", "Multilingual voice responses in English, Hindi & Odia.", "gTTS • LLaMA 3.3 • Speech", "pages/13_Voice_Assistant.py"),
]

for i in range(0, len(features), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(features):
            icon, name, desc, tech, page = features[i + j]
            with col:
                st.markdown(f"""
                <div class="feat-card">
                    <span class="feat-emoji">{icon}</span>
                    <div class="feat-name">{name}</div>
                    <div class="feat-desc">{desc}</div>
                    <span class="feat-tech">⚡ {tech}</span>
                </div>
                """, unsafe_allow_html=True)
                st.page_link(page, label=f"🚀 Open {name}")

# TECH STACK
st.markdown('<div class="sec-title">🛠️ Technology Stack</div>', unsafe_allow_html=True)
tech = {
    "🤖 Machine Learning": ["Random Forest", "Isolation Forest", "Scikit-learn", "XGBoost"],
    "🧠 Generative AI": ["LLaMA 3.3 70B", "Groq API", "Prompt Engineering", "Multi-Agent"],
    "📚 NLP & RAG": ["Sentence Transformers", "ChromaDB", "PyPDF2", "Regex NLP"],
    "📊 Data & Viz": ["Pandas", "NumPy", "Plotly", "ReportLab"],
    "☁️ DevOps": ["GitHub", "Streamlit Cloud", "Python 3.14", "Secrets"],
}
cols = st.columns(5)
for col, (cat, badges) in zip(cols, tech.items()):
    with col:
        st.markdown(f"**<span style='color:#fbbf24;font-size:0.95rem'>{cat}</span>**", unsafe_allow_html=True)
        for b in badges:
            st.markdown(f'<span class="badge">{b}</span>', unsafe_allow_html=True)

# ARCHITECTURE
st.markdown('<div class="sec-title">🏗️ System Architecture</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="arch-card">
    <span style="color:#fbbf24;font-weight:800;font-size:1.1rem;">Platform Layers</span>
    <pre style="color:#e9d5ff;font-size:0.82rem;margin-top:1rem;background:none;border:none;white-space:pre-wrap;">
🔵 ML Layer
  ├── Random Forest (Price Prediction)
  └── Isolation Forest (Fraud Detection)

🟢 NLP Layer
  ├── PyPDF2 + Regex
  └── Rule-based Analysis

🔴 GenAI Layer
  ├── Basic RAG (Keyword)
  ├── Advanced RAG (Semantic)
  │   ├── Sentence Transformers
  │   ├── ChromaDB Vector DB
  │   └── Cosine Similarity
  └── Multi-Agent System (6 Agents)

🟡 Interface Layer
  ├── Streamlit Web App
  ├── PDF Report Generator
  └── Voice Assistant (EN/HI/OD)
    </pre>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="arch-card">
    <span style="color:#fbbf24;font-weight:800;font-size:1.1rem;">Multi-Agent Workflow</span>
    <pre style="color:#e9d5ff;font-size:0.82rem;margin-top:1rem;background:none;border:none;white-space:pre-wrap;">
User Input
    ↓
🏠 Agent 1: Land Valuation
    ↓
⚖️ Agent 2: Legal Verification
    ↓
🚨 Agent 3: Fraud Detection
    ↓
🏗️ Agent 4: Development Analysis
    ↓
📊 Agent 5: Investment Advisory
    ↓
📋 Agent 6: Report Generation
    ↓
✅ Final Intelligence Report
    </pre>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    <div style="font-size:2rem;margin-bottom:0.5rem">🏡</div>
    <span style="font-size:1.2rem;font-weight:800;color:#fbbf24;">BhumiAI</span><br>
    <span style="color:#d8b4fe;">AI Land Intelligence & Legal Verification Platform</span><br><br>
    <span style="color:#c4b5fd;">Developed by </span>
    <span style="color:#fbbf24;font-weight:700;">Aurobinda Biswal</span>
    <span style="color:#c4b5fd;"> | MTech AI & DS | KIIT University, Bhubaneswar, Odisha</span><br>
    <span style="color:#7c3aed;">Built with ❤️ using Python • Streamlit • LLaMA 3.3 70B • ChromaDB • 2026</span>
</div>
""", unsafe_allow_html=True)