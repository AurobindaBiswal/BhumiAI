import streamlit as st

def apply_theme():
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

    /* PAGE HEADER */
    .page-header {
        padding: 2.5rem 2rem;
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(180,100,255,0.2);
        border-radius: 24px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(120,0,255,0.2);
        animation: fadeInDown 0.6s ease;
    }

    .page-title {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #c084fc 0%, #fbbf24 50%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.3rem;
    }

    .page-subtitle {
        font-size: 1rem;
        color: #c4b5fd;
        font-weight: 500;
    }

    /* GLASS CARD */
    .glass-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(168,85,247,0.25);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 20px rgba(120,0,255,0.1);
        animation: fadeInUp 0.5s ease;
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        border-color: rgba(251,191,36,0.4);
        box-shadow: 0 8px 30px rgba(251,191,36,0.15);
        transform: translateY(-2px);
    }

    /* METRIC CARDS */
    .metric-glass {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(168,85,247,0.3);
        border-radius: 16px;
        padding: 1.2rem;
        text-align: center;
        animation: fadeInUp 0.5s ease;
        transition: all 0.3s ease;
    }

    .metric-glass:hover {
        border-color: rgba(251,191,36,0.5);
        transform: translateY(-3px);
    }

    .metric-val {
        font-size: 1.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .metric-lbl {
        font-size: 0.75rem;
        color: #c4b5fd;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.3rem;
    }

    /* RESULT CARDS */
    .result-success {
        background: rgba(34,197,94,0.1);
        border: 1px solid rgba(34,197,94,0.4);
        border-radius: 16px;
        padding: 1.5rem;
        animation: fadeInUp 0.5s ease;
    }

    .result-warning {
        background: rgba(251,191,36,0.1);
        border: 1px solid rgba(251,191,36,0.4);
        border-radius: 16px;
        padding: 1.5rem;
        animation: fadeInUp 0.5s ease;
    }

    .result-danger {
        background: rgba(239,68,68,0.1);
        border: 1px solid rgba(239,68,68,0.4);
        border-radius: 16px;
        padding: 1.5rem;
        animation: fadeInUp 0.5s ease;
    }

    /* SECTION TITLE */
    .sec-head {
        font-size: 1.3rem;
        font-weight: 800;
        color: #ffffff;
        margin: 1.5rem 0 1rem;
        padding-left: 0.8rem;
        border-left: 3px solid #fbbf24;
    }

    /* BUTTONS */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #a855f7) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        padding: 0.6rem 1.5rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(124,58,237,0.4) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #fbbf24, #f59e0b) !important;
        box-shadow: 0 6px 20px rgba(251,191,36,0.4) !important;
        transform: translateY(-2px) !important;
        color: #0d0015 !important;
    }

    /* PRIMARY BUTTON */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #fbbf24, #f59e0b) !important;
        color: #0d0015 !important;
        font-weight: 800 !important;
        box-shadow: 0 4px 20px rgba(251,191,36,0.5) !important;
    }

    /* INPUTS */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(168,85,247,0.4) !important;
        border-radius: 12px !important;
        color: #e9d5ff !important;
        font-weight: 500 !important;
    }

    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {
        border-color: #fbbf24 !important;
        box-shadow: 0 0 0 2px rgba(251,191,36,0.2) !important;
    }

    /* SELECTBOX */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(168,85,247,0.4) !important;
        border-radius: 12px !important;
        color: #e9d5ff !important;
    }

    /* SLIDER */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #7c3aed, #fbbf24) !important;
    }

    /* TABS */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255,255,255,0.04) !important;
        border-radius: 12px !important;
        padding: 0.3rem !important;
        border: 1px solid rgba(168,85,247,0.2) !important;
    }

    .stTabs [data-baseweb="tab"] {
        color: #c4b5fd !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #7c3aed, #a855f7) !important;
        color: white !important;
    }

    /* DATAFRAME */
    .stDataFrame {
        border: 1px solid rgba(168,85,247,0.3) !important;
        border-radius: 12px !important;
    }

    /* EXPANDER */
    .streamlit-expanderHeader {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(168,85,247,0.25) !important;
        border-radius: 12px !important;
        color: #e9d5ff !important;
        font-weight: 600 !important;
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

    /* ALL TEXT */
    .stMarkdown p, .stMarkdown li, label, .stText {
        color: #e9d5ff !important;
    }

    h1, h2, h3 {
        color: #ffffff !important;
    }

    /* CHAT */
    .stChatMessage {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(168,85,247,0.2) !important;
        border-radius: 16px !important;
    }

    /* SUCCESS/ERROR/INFO/WARNING */
    .stSuccess {
        background: rgba(34,197,94,0.1) !important;
        border: 1px solid rgba(34,197,94,0.4) !important;
        border-radius: 12px !important;
        color: #4ade80 !important;
    }

    .stError {
        background: rgba(239,68,68,0.1) !important;
        border: 1px solid rgba(239,68,68,0.4) !important;
        border-radius: 12px !important;
    }

    .stInfo {
        background: rgba(96,165,250,0.1) !important;
        border: 1px solid rgba(96,165,250,0.3) !important;
        border-radius: 12px !important;
        color: #93c5fd !important;
    }

    .stWarning {
        background: rgba(251,191,36,0.1) !important;
        border: 1px solid rgba(251,191,36,0.4) !important;
        border-radius: 12px !important;
        color: #fbbf24 !important;
    }

    /* PAGE LINK */
    a[data-testid="stPageLink-NavLink"] {
        color: #fbbf24 !important;
        font-weight: 700 !important;
        font-size: 0.88rem !important;
        border: 1px solid rgba(251,191,36,0.4) !important;
        border-radius: 10px !important;
        padding: 0.4rem 1rem !important;
        display: inline-block !important;
        margin-top: 0.5rem !important;
        background: rgba(251,191,36,0.1) !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
        text-align: center !important;
    }

    a[data-testid="stPageLink-NavLink"]:hover {
        background: rgba(251,191,36,0.25) !important;
        border-color: #fbbf24 !important;
    }

    a[data-testid="stPageLink-NavLink"] p {
        color: #fbbf24 !important;
        font-weight: 700 !important;
    }

    /* ANIMATIONS */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.6; }
    }

    @keyframes shimmer {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }
    </style>
    """, unsafe_allow_html=True)


def page_header(icon, title, subtitle):
    st.markdown(f"""
    <div class="page-header">
        <div class="page-title">{icon} {title}</div>
        <div class="page-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def metric_card(value, label):
    st.markdown(f"""
    <div class="metric-glass">
        <div class="metric-val">{value}</div>
        <div class="metric-lbl">{label}</div>
    </div>
    """, unsafe_allow_html=True)


def glass_card(content):
    st.markdown(f'<div class="glass-card">{content}</div>', unsafe_allow_html=True)


def sec_head(title):
    st.markdown(f'<div class="sec-head">{title}</div>', unsafe_allow_html=True)