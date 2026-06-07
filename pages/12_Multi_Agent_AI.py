import sys
sys.path.append('.')
from theme import apply_theme, page_header, sec_head
import streamlit as st
from groq import Groq
import json
import time

st.set_page_config(page_title="Multi-Agent AI", page_icon="🤖", layout="wide")
apply_theme()

page_header("🤝", "Multi-Agent AI Land Intelligence System", "6 specialized AI agents collaborate to provide comprehensive land analysis.")

# --- PUT YOUR GROQ API KEY HERE ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_API_KEY = "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"
# ----------------------------------

client = Groq(api_key=GROQ_API_KEY)

def run_agent(agent_name, agent_role, task, context="", temperature=0.3):
    system_prompt = f"""You are {agent_name}, a specialized AI agent for land intelligence.
Your role: {agent_role}
Be concise, professional, and provide actionable insights.
Format your response with clear sections and bullet points.
Focus only on your specialization."""

    user_message = f"{task}"
    if context:
        user_message += f"\n\nContext from previous agents:\n{context}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=600,
        temperature=temperature
    )
    return response.choices[0].message.content

# Agent definitions
AGENTS = [
    {
        "id": 1,
        "name": "🏠 Land Valuation Agent",
        "role": "Expert in Indian land price analysis, market trends, and property valuation",
        "color": "#1a5276",
        "icon": "🏠"
    },
    {
        "id": 2,
        "name": "⚖️ Legal Verification Agent",
        "role": "Expert in Indian land laws, document verification, Odisha land records, RERA regulations",
        "color": "#1e8449",
        "icon": "⚖️"
    },
    {
        "id": 3,
        "name": "🚨 Fraud Detection Agent",
        "role": "Expert in detecting land fraud, suspicious transactions, ownership anomalies",
        "color": "#922b21",
        "icon": "🚨"
    },
    {
        "id": 4,
        "name": "🏗️ Development Analysis Agent",
        "role": "Expert in land development potential, zoning, infrastructure assessment",
        "color": "#784212",
        "icon": "🏗️"
    },
    {
        "id": 5,
        "name": "📊 Investment Advisory Agent",
        "role": "Expert in real estate investment analysis, ROI calculation, market trends",
        "color": "#6c3483",
        "icon": "📊"
    },
    {
        "id": 6,
        "name": "📋 Report Generation Agent",
        "role": "Expert in synthesizing all agent outputs into a comprehensive final report",
        "color": "#117a65",
        "icon": "📋"
    }
]

# Initialize session state
if "agent_results" not in st.session_state:
    st.session_state.agent_results = {}
if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

st.markdown("---")

# Architecture diagram
with st.expander("🏗️ Multi-Agent Architecture", expanded=False):
    st.markdown("""Each agent receives output from previous agents as context — **collaborative intelligence!**
    """)

st.subheader("📝 Enter Land Details for Multi-Agent Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    location = st.text_input("Property Location", "Patia, Bhubaneswar, Odisha")
    area = st.number_input("Area (sq ft)", min_value=100, max_value=100000, value=2400)
    asking_price = st.number_input("Asking Price (₹)", min_value=100000, max_value=100000000, value=4500000, step=100000)

with col2:
    land_type = st.selectbox("Land Type", ["Residential", "Commercial", "Agricultural", "Industrial"])
    zone = st.selectbox("Zone", ["Urban", "Semi-Urban", "Rural"])
    years_owned = st.number_input("Years Owned by Seller", min_value=0, max_value=100, value=5)

with col3:
    legal_issues = st.selectbox("Known Legal Issues", ["None", "Minor disputes", "Major disputes", "Unclear title"])
    infrastructure = st.slider("Infrastructure Quality (1-10)", 1, 10, 7)
    market_trend = st.selectbox("Market Trend", ["Rising", "Stable", "Declining"])

land_details = f"""
Property Location: {location}
Area: {area} sq ft
Asking Price: ₹{asking_price:,}
Land Type: {land_type}
Zone: {zone}
Years owned by seller: {years_owned}
Legal issues: {legal_issues}
Infrastructure quality: {infrastructure}/10
Market trend: {market_trend}
Price per sq ft: ₹{asking_price//area:,}
"""

if st.button("🚀 Run Multi-Agent Analysis", type="primary"):
    st.session_state.agent_results = {}
    st.session_state.analysis_complete = False

    st.markdown("---")
    st.subheader("🤖 Agents Working...")

    cumulative_context = f"Land Details:\n{land_details}"

    for i, agent in enumerate(AGENTS):
        with st.spinner(f"Running {agent['name']}..."):
            
            if agent['id'] == 1:
                task = f"Analyze the market value and pricing for this land: {land_details}. Is the asking price fair? What should be the market value?"
            elif agent['id'] == 2:
                task = f"Verify the legal status and document requirements for this land: {land_details}. What legal checks are needed?"
            elif agent['id'] == 3:
                task = f"Assess fraud risk for this land transaction: {land_details}. Any red flags?"
            elif agent['id'] == 4:
                task = f"Analyze development potential for this land: {land_details}. What is the best use?"
            elif agent['id'] == 5:
                task = f"Provide investment recommendation for this land: {land_details}. Should the buyer invest?"
            else:
                task = f"Generate a final comprehensive report synthesizing all agent findings for: {land_details}"

            result = run_agent(agent['name'], agent['role'], task, cumulative_context)
            st.session_state.agent_results[agent['id']] = result
            cumulative_context += f"\n\n{agent['name']} Output:\n{result}"

            # Show result immediately
            with st.expander(f"{agent['icon']} {agent['name']} — ✅ Complete", expanded=(i==5)):
                st.markdown(result)

            time.sleep(0.5)

    st.session_state.analysis_complete = True
    st.success("✅ All 6 Agents Complete! Scroll down for Final Report.")

# Show final report
if st.session_state.analysis_complete and 6 in st.session_state.agent_results:
    st.markdown("---")
    st.subheader("📋 Final Intelligence Report")
    st.markdown(st.session_state.agent_results[6])

    # Summary metrics
    st.markdown("---")
    st.subheader("📊 Agent Summary")
    cols = st.columns(6)
    for i, (agent, col) in enumerate(zip(AGENTS, cols)):
        with col:
            st.metric(agent['icon'], agent['name'].split(' ', 1)[1], "✅ Done")