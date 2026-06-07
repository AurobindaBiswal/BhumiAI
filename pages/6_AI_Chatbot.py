import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Land Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 AI Land Intelligence Chatbot")
st.write("Ask anything about land buying, selling, legal verification, investment, and more.")


GROQ_API_KEY = "gsk"


SYSTEM_PROMPT = """You are an expert AI assistant specializing in Indian land and real estate intelligence. 
You have deep knowledge about:
- Land valuation and price prediction across Indian states especially Odisha
- Legal document verification for land transactions (Sale Deed, Title Deed, etc.)
- Fraud detection in land transactions
- Land investment analysis and ROI calculation
- Development potential assessment
- Indian land laws, registration process, stamp duty
- Odisha specific land records (Bhulekh), RoR (Record of Rights)
- RERA regulations for real estate
- Negotiation strategies for land deals

Always provide practical, accurate advice. When discussing prices, refer to Indian market rates.
Keep responses clear, structured and helpful. Use bullet points where appropriate.
Always recommend consulting a legal expert for final decisions."""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.subheader("💬 Chat Options")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.subheader("💡 Sample Questions")
    sample_questions = [
        "How to verify land documents in Odisha?",
        "What is stamp duty for land in Odisha?",
        "How to check if land has legal disputes?",
        "What documents needed for land purchase?",
        "How to calculate land investment ROI?",
        "What is Bhulekh in Odisha?",
        "Red flags in land transactions?",
        "How to negotiate land price?"
    ]
    
    for question in sample_questions:
        if st.button(question, key=question):
            st.session_state.messages.append({"role": "user", "content": question})
            try:
                client = Groq(api_key=GROQ_API_KEY)
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages,
                    max_tokens=1000,
                    temperature=0.7
                )
                answer = response.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": f"Error: {str(e)}. Please check your API key."
                })
            st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask about land investment, legal docs, fraud detection..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                client = Groq(api_key=GROQ_API_KEY)
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages,
                    max_tokens=1000,
                    temperature=0.7
                )
                answer = response.choices[0].message.content
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                error_msg = f"Error: {str(e)}. Please check your API key."
                st.write(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})