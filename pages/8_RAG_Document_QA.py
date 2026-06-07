import streamlit as st
import PyPDF2
import io
from groq import Groq

st.set_page_config(page_title="RAG Document Q&A", page_icon="🔍", layout="wide")

st.title("🔍 RAG — Document Intelligence Q&A")
st.write("Upload land documents and ask questions. AI will answer based on document content.")

# --- PUT YOUR GROQ API KEY HERE ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
# ----------------------------------

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for i, page in enumerate(pdf_reader.pages):
        text += f"\n--- Page {i+1} ---\n"
        text += page.extract_text()
    return text

def extract_text_from_txt(txt_file):
    return txt_file.read().decode('utf-8')

def chunk_text(text, chunk_size=2000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks

def find_relevant_chunks(chunks, question, max_chunks=3):
    question_words = set(question.lower().split())
    scored_chunks = []
    for i, chunk in enumerate(chunks):
        chunk_words = set(chunk.lower().split())
        score = len(question_words.intersection(chunk_words))
        scored_chunks.append((score, i, chunk))
    scored_chunks.sort(reverse=True)
    return [chunk for _, _, chunk in scored_chunks[:max_chunks]]

def answer_question(context, question, chat_history):
    client = Groq(api_key=GROQ_API_KEY)
    
    system_prompt = """You are an expert AI assistant for Indian land and legal document analysis.
You answer questions ONLY based on the provided document context.
If the answer is not in the document, say "This information is not found in the uploaded document."
Always be precise, cite relevant details from the document, and provide helpful insights.
For legal documents, highlight important clauses, dates, amounts, and parties involved."""

    messages = [{"role": "system", "content": system_prompt}]
    
    # Add chat history
    for msg in chat_history[-4:]:
        messages.append(msg)
    
    # Add current question with context
    user_message = f"""Document Context:
{context}

Question: {question}

Please answer based on the document context above."""
    
    messages.append({"role": "user", "content": user_message})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=1000,
        temperature=0.3
    )
    return response.choices[0].message.content

# Initialize session state
if "rag_messages" not in st.session_state:
    st.session_state.rag_messages = []
if "document_chunks" not in st.session_state:
    st.session_state.document_chunks = []
if "document_name" not in st.session_state:
    st.session_state.document_name = None
if "full_text" not in st.session_state:
    st.session_state.full_text = ""

# Sidebar
with st.sidebar:
    st.subheader("📁 Upload Document")
    uploaded_file = st.file_uploader("Upload Land Document", type=['pdf', 'txt'])
    
    if uploaded_file:
        if uploaded_file.name != st.session_state.document_name:
            with st.spinner("Processing document..."):
                if uploaded_file.type == "application/pdf":
                    text = extract_text_from_pdf(uploaded_file)
                else:
                    text = extract_text_from_txt(uploaded_file)
                
                st.session_state.full_text = text
                st.session_state.document_chunks = chunk_text(text)
                st.session_state.document_name = uploaded_file.name
                st.session_state.rag_messages = []
            st.success(f"✅ Document processed! {len(st.session_state.document_chunks)} chunks created.")
    
    if st.session_state.document_name:
        st.info(f"📄 Active: {st.session_state.document_name}")
        st.metric("Text Chunks", len(st.session_state.document_chunks))
        st.metric("Total Characters", len(st.session_state.full_text))
    
    st.markdown("---")
    st.subheader("💡 Sample Questions")
    sample_qs = [
        "Who are the parties in this document?",
        "What is the total land area?",
        "What is the transaction amount?",
        "Are there any legal disputes mentioned?",
        "What are the plot/survey numbers?",
        "What is the registration date?",
        "Is stamp duty mentioned?",
        "What are the boundary details?",
        "Are there any encumbrances?",
        "Summarize this document"
    ]
    for q in sample_qs:
        if st.button(q, key=f"sq_{q}"):
            if st.session_state.document_chunks:
                relevant = find_relevant_chunks(st.session_state.document_chunks, q)
                context = "\n\n".join(relevant)
                st.session_state.rag_messages.append({"role": "user", "content": q})
                try:
                    answer = answer_question(context, q, st.session_state.rag_messages[:-1])
                    st.session_state.rag_messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.session_state.rag_messages.append({"role": "assistant", "content": f"Error: {str(e)}"})
                st.rerun()
            else:
                st.warning("Please upload a document first!")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.rag_messages = []
        st.rerun()

# Main area
if not st.session_state.document_chunks:
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        ### 📖 How RAG Works
        
        **RAG = Retrieval Augmented Generation**
        
        1. 📤 **Upload** your land document (PDF/TXT)
        2. 🔪 **Chunking** — Document split into chunks
        3. 🔍 **Retrieval** — Relevant chunks found for your question
        4. 🤖 **Generation** — LLM answers using retrieved context
        
        This ensures AI answers are grounded in YOUR document!
        """)
    with col2:
        st.success("""
        ### 📄 Supported Documents
        
        - ✅ Sale Deed
        - ✅ Title Deed  
        - ✅ Lease Agreement
        - ✅ Mortgage Deed
        - ✅ Gift Deed
        - ✅ Power of Attorney
        - ✅ Land Survey Reports
        - ✅ Any land-related PDF
        """)
    
    # Demo mode
    st.markdown("---")
    st.subheader("🧪 Try Demo — No Upload Needed")
    
    demo_doc = """
SALE DEED - DEMO DOCUMENT

Executed on 15th March 2024 at Bhubaneswar, Odisha.

VENDOR: Shri Ramesh Kumar Patel, S/o Shri Suresh Patel
Address: Plot No. 45, Patia, Bhubaneswar, Odisha - 751024
Aadhaar: XXXX-XXXX-1234, PAN: ABCDE1234F

VENDEE: Smt. Priya Singh, D/o Shri Mohan Singh  
Address: Survey No. 123, Cuttack, Odisha - 753001
Aadhaar: XXXX-XXXX-5678, PAN: FGHIJ5678K

PROPERTY DETAILS:
Plot No. 234, Survey No. 456/B, Khasra No. 789
Location: Patia, Bhubaneswar, Khordha District, Odisha
Total Area: 2400 Square Feet (223 Square Meters)
Boundaries: North - Road, South - Plot 235, East - Plot 233, West - Canal

CONSIDERATION:
Total Sale Amount: Rs. 45,00,000 (Rupees Forty Five Lakhs Only)
Advance Paid: Rs. 5,00,000 on 01/02/2024
Balance Amount: Rs. 40,00,000 paid on date of registration

STAMP DUTY & REGISTRATION:
Stamp Duty Paid: Rs. 2,25,000 (5% of sale value)
Registration Fee: Rs. 45,000 (1% of sale value)
Registered at: Sub-Registrar Office, Bhubaneswar
Registration Date: 15/03/2024
Document No: SR/BBR/2024/1234

DECLARATIONS:
The vendor declares the property is free from all encumbrances, 
mortgages, disputes and litigation. Clear title is hereby transferred.

WITNESSES:
1. Shri Ajay Kumar Verma, Advocate
2. Smt. Kavita Sharma, Notary Public
"""
    
    demo_question = st.text_input("Ask about the demo document:", 
                                   placeholder="e.g. What is the sale amount?")
    
    if st.button("🔍 Ask Demo Question", type="primary"):
        if demo_question:
            with st.spinner("Analyzing..."):
                try:
                    answer = answer_question(demo_doc, demo_question, [])
                    st.success(f"**Q: {demo_question}**")
                    st.write(f"**A:** {answer}")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a question!")

else:
    # Chat interface
    st.subheader(f"💬 Chat with: {st.session_state.document_name}")
    
    for message in st.session_state.rag_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    if prompt := st.chat_input("Ask anything about your document..."):
        st.session_state.rag_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Searching document and generating answer..."):
                try:
                    relevant_chunks = find_relevant_chunks(
                        st.session_state.document_chunks, prompt
                    )
                    context = "\n\n".join(relevant_chunks)
                    answer = answer_question(context, prompt, st.session_state.rag_messages[:-1])
                    st.write(answer)
                    st.session_state.rag_messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    error_msg = f"Error: {str(e)}"
                    st.write(error_msg)
                    st.session_state.rag_messages.append({"role": "assistant", "content": error_msg})