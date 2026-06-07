import sys
sys.path.append('.')
from theme import apply_theme, page_header, sec_head
import streamlit as st
import io
import os
from groq import Groq
from gtts import gTTS
import base64

st.set_page_config(page_title="Voice Assistant", page_icon="🗣️", layout="wide")
apply_theme()

page_header("🗣️", "BhumiAI Voice Assistant", "Multilingual voice assistant for land queries — English, Hindi, and Odia supported.")

# --- PUT YOUR GROQ API KEY HERE ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_API_KEY = "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"
# ----------------------------------

SYSTEM_PROMPT = """You are BhumiAI Voice Assistant, an expert in Indian land and real estate.
You specialize in Odisha land records, legal documents, investment advice, and fraud detection.
Keep responses concise (2-3 sentences max) since they will be spoken aloud.
Be helpful, clear, and professional."""

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

def get_ai_response(question, language):
    client = Groq(api_key=GROQ_API_KEY)
    
    lang_instruction = ""
    if language == "Hindi":
        lang_instruction = "Respond in Hindi language."
    elif language == "Odia":
        lang_instruction = "Respond in Odia language if possible, otherwise English."
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT + " " + lang_instruction},
            {"role": "user", "content": question}
        ],
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].message.content

def autoplay_audio(audio_buffer):
    audio_bytes = audio_buffer.read()
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

# Initialize session state
if "voice_messages" not in st.session_state:
    st.session_state.voice_messages = []

st.markdown("---")

# Language selector
col1, col2, col3 = st.columns(3)
with col1:
    language = st.selectbox("🌐 Select Language", ["English", "Hindi", "Odia"])
with col2:
    tts_lang = {"English": "en", "Hindi": "hi", "Odia": "en"}[language]
    st.metric("TTS Language", language)
with col3:
    st.metric("AI Model", "LLaMA 3.3 70B")

st.markdown("---")

# Sample questions
st.subheader("💡 Quick Questions — Click to Ask")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**🇬🇧 English**")
    eng_questions = [
        "Is land near KIIT a good investment?",
        "What documents needed to buy land?",
        "How to check land fraud in Odisha?",
        "What is stamp duty in Odisha?",
    ]
    for q in eng_questions:
        if st.button(q, key=f"eng_{q}"):
            with st.spinner("AI thinking..."):
                answer = get_ai_response(q, "English")
                st.session_state.voice_messages.append({"role": "user", "content": q, "lang": "English"})
                st.session_state.voice_messages.append({"role": "assistant", "content": answer, "lang": "English"})
                audio = text_to_speech(answer, 'en')
                autoplay_audio(audio)
            st.rerun()

with col2:
    st.write("**🇮🇳 Hindi**")
    hindi_questions = [
        "भुवनेश्वर में जमीन कैसे खरीदें?",
        "जमीन की कीमत कैसे पता करें?",
        "क्या ओडिशा में निवेश अच्छा है?",
        "जमीन के दस्तावेज कैसे चेक करें?",
    ]
    for q in hindi_questions:
        if st.button(q, key=f"hin_{q}"):
            with st.spinner("AI सोच रहा है..."):
                answer = get_ai_response(q, "Hindi")
                st.session_state.voice_messages.append({"role": "user", "content": q, "lang": "Hindi"})
                st.session_state.voice_messages.append({"role": "assistant", "content": answer, "lang": "Hindi"})
                audio = text_to_speech(answer, 'hi')
                autoplay_audio(audio)
            st.rerun()

with col3:
    st.write("**🏛️ Odia**")
    odia_questions = [
        "ଭୁବନେଶ୍ୱରରେ ଜମି କିଣିବା ଉଚିତ?",
        "ଜମି ଦଲିଲ କିପରି ଯାଞ୍ଚ କରିବେ?",
        "ଓଡ଼ିଶାରେ ସ୍ଟ୍ୟାମ୍ପ ଡ୍ୟୁଟି କେତେ?",
        "ଜମି ଠକାମି କିପରି ଚିହ୍ନିବେ?",
    ]
    for q in odia_questions:
        if st.button(q, key=f"odi_{q}"):
            with st.spinner("AI ଭାବୁଛି..."):
                answer = get_ai_response(q, "Odia")
                st.session_state.voice_messages.append({"role": "user", "content": q, "lang": "Odia"})
                st.session_state.voice_messages.append({"role": "assistant", "content": answer, "lang": "Odia"})
                audio = text_to_speech(answer, 'en')
                autoplay_audio(audio)
            st.rerun()

st.markdown("---")

# Text input
st.subheader("💬 Type Your Question")
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input("Ask anything about land...", 
                                placeholder="e.g. What is Bhulekh in Odisha?")
with col2:
    st.write("")
    st.write("")
    ask_button = st.button("🔊 Ask & Speak", type="primary")

if ask_button and user_input:
    with st.spinner("AI generating voice response..."):
        answer = get_ai_response(user_input, language)
        st.session_state.voice_messages.append({"role": "user", "content": user_input, "lang": language})
        st.session_state.voice_messages.append({"role": "assistant", "content": answer, "lang": language})
        audio = text_to_speech(answer, tts_lang)
        autoplay_audio(audio)
    st.rerun()

st.markdown("---")

# Chat history
if st.session_state.voice_messages:
    st.subheader("📜 Conversation History")
    
    if st.button("🗑️ Clear History"):
        st.session_state.voice_messages = []
        st.rerun()
    
    for msg in reversed(st.session_state.voice_messages):
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(f"[{msg['lang']}] {msg['content']}")
        else:
            with st.chat_message("assistant"):
                st.write(msg['content'])
                # Replay button
                if st.button(f"🔊 Replay", key=f"replay_{msg['content'][:20]}"):
                    lang_code = {"English": "en", "Hindi": "hi", "Odia": "en"}[msg['lang']]
                    audio = text_to_speech(msg['content'], lang_code)
                    autoplay_audio(audio)