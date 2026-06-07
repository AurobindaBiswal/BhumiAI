import streamlit as st
import PyPDF2
import io
import os
from groq import Groq

st.set_page_config(page_title="Advanced RAG", page_icon="🔍", layout="wide")

st.title("🔍 Advanced RAG — Semantic Document Intelligence")
st.write("Enterprise-grade RAG using Sentence Transformers + ChromaDB vector database.")

# --- PUT YOUR GROQ API KEY HERE ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_API_KEY = "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"
# ----------------------------------

@st.cache_resource
def load_embedding_model():
    from sentence_transformers import SentenceTransformer
    with st.spinner("Loading embedding model... (first time only, ~30 seconds)"):
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def get_chroma_client():
    import chromadb
    client = chromadb.Client()
    return client

def extract_text(file):
    if file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for i, page in enumerate(pdf_reader.pages):
            text += f"\n--- Page {i+1} ---\n{page.extract_text()}"
        return text
    else:
        return file.read().decode('utf-8')

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks

def semantic_search(query, chunks, embeddings_model, top_k=3):
    import numpy as np
    query_embedding = embeddings_model.encode([query])[0]
    chunk_embeddings = embeddings_model.encode(chunks)
    
    # Cosine similarity
    similarities = []
    for i, chunk_emb in enumerate(chunk_embeddings):
        dot_product = np.dot(query_embedding, chunk_emb)
        norm_q = np.linalg.norm(query_embedding)
        norm_c = np.linalg.norm(chunk_emb)
        similarity = dot_product / (norm_q * norm_c) if norm_q * norm_c > 0 else 0
        similarities.append((similarity, i, chunks[i]))
    
    similarities.sort(reverse=True)
    return similarities[:top_k]

def generate_answer(context, question):
    client = Groq(api_key=GROQ_API_KEY)
    
    system_prompt = """You are an expert AI assistant for Indian land and legal document analysis.
Answer questions ONLY based on the provided document context.
If the answer is not found, say "This information is not in the document."
Be precise, cite specific details, and provide helpful insights about land transactions."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Document Context:\n{context}\n\nQuestion: {question}"}
        ],
        max_tokens=800,
        temperature=0.3
    )
    return response.choices[0].message.content

# Initialize session state
if "adv_rag_messages" not in st.session_state:
    st.session_state.adv_rag_messages = []
if "adv_chunks" not in st.session_state:
    st.session_state.adv_chunks = []
if "adv_doc_name" not in st.session_state:
    st.session_state.adv_doc_name = None

# How RAG works explanation
with st.expander("🧠 How Advanced RAG Works", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Basic RAG (Old System)
        - ❌ Keyword matching only
        - ❌ Misses synonyms & context
        - ❌ No semantic understanding
        - Example: Search "price" misses "cost", "value", "amount"
        """)
    with col2:
        st.markdown("""
        ### Advanced RAG (This System)
        - ✅ **Sentence Transformers** — semantic embeddings
        - ✅ **Cosine Similarity** — finds contextually similar chunks
        - ✅ **ChromaDB** — vector database storage
        - ✅ Understands meaning, not just keywords!
        - Example: Search "price" also finds "cost", "valuation", "amount"
        """)

st.markdown("---")

# Sidebar
with st.sidebar:
    st.subheader("📁 Upload Document")
    uploaded_file = st.file_uploader("Upload Land Document (PDF/TXT)", type=['pdf', 'txt'])

    if uploaded_file:
        if uploaded_file.name != st.session_state.adv_doc_name:
            with st.spinner("Processing with Semantic Embeddings..."):
                text = extract_text(uploaded_file)
                chunks = chunk_text(text)
                st.session_state.adv_chunks = chunks
                st.session_state.adv_doc_name = uploaded_file.name
                st.session_state.adv_rag_messages = []
            st.success(f"✅ {len(chunks)} semantic chunks created!")

    if st.session_state.adv_doc_name:
        st.info(f"📄 Active: {st.session_state.adv_doc_name}")
        st.metric("Chunks Created", len(st.session_state.adv_chunks))
        st.metric("Embedding Model", "MiniLM-L6-v2")
        st.metric("Vector Dimensions", "384")

    st.markdown("---")
    st.subheader("💡 Sample Questions")
    sample_qs = [
        "Who are the parties involved?",
        "What is the property value?",
        "Are there any legal disputes?",
        "What are the boundary details?",
        "Summarize this document",
        "What documents are required?",
        "Is there any encumbrance?",
    ]
    for q in sample_qs:
        if st.button(q, key=f"aq_{q}"):
            if st.session_state.adv_chunks:
                st.session_state.adv_rag_messages.append({"role": "user", "content": q})
                try:
                    model = load_embedding_model()
                    results = semantic_search(q, st.session_state.adv_chunks, model)
                    context = "\n\n".join([chunk for _, _, chunk in results])
                    answer = generate_answer(context, q)
                    
                    # Show similarity scores
                    scores_text = " | ".join([f"Chunk {i+1}: {sim:.3f}" for i, (sim, _, _) in enumerate(results)])
                    full_answer = f"{answer}\n\n*Semantic Similarity Scores: {scores_text}*"
                    st.session_state.adv_rag_messages.append({"role": "assistant", "content": full_answer})
                except Exception as e:
                    st.session_state.adv_rag_messages.append({"role": "assistant", "content": f"Error: {str(e)}"})
                st.rerun()
            else:
                st.warning("Upload a document first!")

    if st.button("🗑️ Clear Chat"):
        st.session_state.adv_rag_messages = []
        st.rerun()

# Main area
if not st.session_state.adv_chunks:
    st.subheader("🧪 Demo — No Upload Needed")
    st.info("Try the semantic search on a sample Odisha land document!")

    demo_doc = """
SALE DEED - BHUBANESWAR, ODISHA

This Sale Deed is executed on 15th March 2024 between:

VENDOR: Shri Ramesh Kumar Patel, Son of Shri Suresh Patel
Address: Plot No. 45, Patia, Bhubaneswar, Odisha - 751024
Aadhaar: XXXX-XXXX-1234, PAN: ABCDE1234F

VENDEE: Smt. Priya Singh, Daughter of Shri Mohan Singh
Address: Survey No. 123, Cuttack, Odisha - 753001

PROPERTY DETAILS:
Plot No. 234, Survey No. 456/B, Khasra No. 789
Location: Patia, Bhubaneswar, Khordha District, Odisha
Total Area: 2400 Square Feet
Boundaries: North - Road, South - Plot 235, East - Plot 233, West - Canal

FINANCIAL DETAILS:
Total Sale Amount: Rs. 45,00,000 (Forty Five Lakhs Only)
Advance Paid: Rs. 5,00,000 on 01/02/2024
Balance: Rs. 40,00,000 paid on registration date
Stamp Duty: Rs. 2,25,000 (5% of sale value)
Registration Fee: Rs. 45,000

LEGAL DECLARATIONS:
The vendor declares the property is free from all encumbrances,
mortgages, disputes and litigation. Clear title transferred.
No pending loans or legal cases on this property.

WITNESSES:
1. Shri Ajay Kumar Verma, Advocate
2. Smt. Kavita Sharma, Notary Public
"""

    demo_question = st.text_input("Ask a question about the demo document:",
                                   placeholder="e.g. What is the total sale amount?")

    if st.button("🔍 Search Semantically", type="primary"):
        if demo_question:
            with st.spinner("Running semantic search..."):
                try:
                    model = load_embedding_model()
                    demo_chunks = chunk_text(demo_doc, chunk_size=100, overlap=10)
                    results = semantic_search(demo_question, demo_chunks, model)
                    context = "\n\n".join([chunk for _, _, chunk in results])

                    st.subheader("🔍 Retrieved Context (Semantic Search)")
                    for i, (sim, idx, chunk) in enumerate(results):
                        with st.expander(f"Chunk {i+1} — Similarity: {sim:.4f}"):
                            st.write(chunk)

                    st.subheader("🤖 AI Answer")
                    answer = generate_answer(context, demo_question)
                    st.success(answer)

                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a question!")

else:
    st.subheader(f"💬 Semantic Chat: {st.session_state.adv_doc_name}")

    for message in st.session_state.adv_rag_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Ask anything — semantic search will find relevant context..."):
        st.session_state.adv_rag_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Semantic search + AI generation..."):
                try:
                    model = load_embedding_model()
                    results = semantic_search(prompt, st.session_state.adv_chunks, model)
                    context = "\n\n".join([chunk for _, _, chunk in results])

                    # Show retrieved chunks
                    with st.expander("📚 Retrieved Chunks (Semantic Search)"):
                        for i, (sim, idx, chunk) in enumerate(results):
                            st.write(f"**Chunk {i+1} — Similarity: {sim:.4f}**")
                            st.write(chunk[:200] + "...")
                            st.markdown("---")

                    answer = generate_answer(context, prompt)
                    st.write(answer)
                    st.session_state.adv_rag_messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    error_msg = f"Error: {str(e)}"
                    st.write(error_msg)
                    st.session_state.adv_rag_messages.append({"role": "assistant", "content": error_msg})