import streamlit as st
import PyPDF2
import io
import re

st.set_page_config(page_title="Legal Document Analyzer", page_icon="📄", layout="wide")

st.title("📄 Legal Document Analyzer")
st.write("Upload land-related legal documents for AI-powered analysis and verification.")

# Analysis functions
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def analyze_document(text):
    results = {}
    
    # Document type detection
    doc_types = {
        'Sale Deed': ['sale deed', 'vendor', 'vendee', 'sold', 'purchased'],
        'Title Deed': ['title deed', 'title', 'ownership', 'proprietor'],
        'Lease Agreement': ['lease', 'lessee', 'lessor', 'rent', 'tenancy'],
        'Mortgage Deed': ['mortgage', 'mortgagor', 'mortgagee', 'loan', 'hypothecation'],
        'Gift Deed': ['gift deed', 'donor', 'donee', 'gifted'],
        'Power of Attorney': ['power of attorney', 'attorney', 'authorize', 'principal'],
        'Land Survey': ['survey', 'plot number', 'khasra', 'khata', 'survey number'],
    }
    
    text_lower = text.lower()
    detected_type = "Unknown Document"
    for doc_type, keywords in doc_types.items():
        if any(keyword in text_lower for keyword in keywords):
            detected_type = doc_type
            break
    results['document_type'] = detected_type
    
    # Extract key information
    # Dates
    date_pattern = r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{1,2}\s+\w+\s+\d{4})\b'
    dates = re.findall(date_pattern, text)
    results['dates'] = list(set(dates))[:5]
    
    # Amounts
    amount_pattern = r'(?:Rs\.?|INR|₹)\s*[\d,]+(?:\.\d{2})?'
    amounts = re.findall(amount_pattern, text, re.IGNORECASE)
    results['amounts'] = list(set(amounts))[:5]
    
    # Plot/Survey numbers
    plot_pattern = r'(?:plot|survey|khasra|khata|dag)\s*(?:no\.?|number)?\s*[\d/\-]+'
    plots = re.findall(plot_pattern, text, re.IGNORECASE)
    results['plot_numbers'] = list(set(plots))[:5]
    
    # Names (simple heuristic)
    name_pattern = r'(?:Mr\.|Mrs\.|Ms\.|Dr\.|Shri|Smt\.)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*'
    names = re.findall(name_pattern, text)
    results['parties'] = list(set(names))[:6]
    
    # Red flags
    red_flags = []
    red_flag_keywords = {
        'Disputed ownership mentioned': ['dispute', 'disputed', 'litigation', 'court case'],
        'Encumbrance detected': ['encumbrance', 'mortgage', 'loan', 'hypothecated'],
        'Missing registration details': ['unregistered', 'not registered'],
        'Boundary dispute risk': ['boundary', 'encroachment', 'trespass'],
        'Multiple ownership claims': ['joint ownership', 'co-owner', 'multiple owners'],
    }
    
    for flag, keywords in red_flag_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            red_flags.append(flag)
    results['red_flags'] = red_flags
    
    # Legal compliance checks
    compliance = {
        'Stamp Duty Mentioned': any(k in text_lower for k in ['stamp duty', 'stamp paper']),
        'Registration Details Present': any(k in text_lower for k in ['registered', 'registration', 'sub-registrar']),
        'Witness Signatures': any(k in text_lower for k in ['witness', 'witnesses', 'attested']),
        'Notarization': any(k in text_lower for k in ['notary', 'notarized', 'notarisation']),
        'Survey Number Present': any(k in text_lower for k in ['survey no', 'survey number', 'khasra']),
    }
    results['compliance'] = compliance
    
    # Overall score
    compliance_score = sum(compliance.values()) / len(compliance) * 100
    flag_penalty = len(red_flags) * 10
    results['overall_score'] = max(0, min(100, compliance_score - flag_penalty))
    
    return results

# Demo text for testing
demo_text = """
SALE DEED

This Sale Deed is executed on 15th March 2024 between:

VENDOR: Shri Ramesh Kumar Patel, Son of Shri Suresh Patel, 
residing at Plot No. 45, Bhubaneswar, Odisha - 751001

VENDEE: Smt. Priya Singh, Daughter of Shri Mohan Singh,
residing at Survey No. 123, Cuttack, Odisha - 753001

PROPERTY DETAILS:
Plot No. 234, Survey No. 456/B, Khasra No. 789
Located at: Patia, Bhubaneswar, Odisha
Area: 2400 Square Feet

CONSIDERATION AMOUNT: Rs. 45,00,000 (Forty Five Lakhs Only)
Stamp Duty Paid: Rs. 2,25,000

This deed is registered before the Sub-Registrar, Bhubaneswar.
Witnesses: 1. Shri Ajay Verma  2. Smt. Kavita Sharma

The vendor hereby declares that the property is free from 
all encumbrances, disputes and litigation.
"""

# UI
tab1, tab2 = st.tabs(["📤 Upload Document", "🧪 Try Demo"])

with tab1:
    uploaded_file = st.file_uploader("Upload Legal Document (PDF)", type=['pdf'])
    
    if uploaded_file is not None:
        with st.spinner("Analyzing document..."):
            text = extract_text_from_pdf(uploaded_file)
            if text.strip():
                results = analyze_document(text)
                
                st.success("✅ Document analyzed successfully!")
                
                # Show results
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Document Type", results['document_type'])
                with col2:
                    score = results['overall_score']
                    color = "🟢" if score >= 70 else "🟡" if score >= 40 else "🔴"
                    st.metric("Legal Score", f"{color} {score:.0f}/100")
                
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📋 Extracted Information")
                    if results['parties']:
                        st.write("**Parties Involved:**")
                        for p in results['parties']:
                            st.write(f"• {p}")
                    if results['dates']:
                        st.write("**Dates Found:**")
                        for d in results['dates']:
                            st.write(f"• {d}")
                    if results['amounts']:
                        st.write("**Amounts Found:**")
                        for a in results['amounts']:
                            st.write(f"• {a}")
                    if results['plot_numbers']:
                        st.write("**Plot/Survey Numbers:**")
                        for p in results['plot_numbers']:
                            st.write(f"• {p}")
                
                with col2:
                    st.subheader("✅ Compliance Check")
                    for check, status in results['compliance'].items():
                        icon = "✅" if status else "❌"
                        st.write(f"{icon} {check}")
                    
                    st.subheader("⚠️ Red Flags")
                    if results['red_flags']:
                        for flag in results['red_flags']:
                            st.warning(f"⚠️ {flag}")
                    else:
                        st.success("✅ No red flags detected!")
            else:
                st.error("Could not extract text from PDF. Please try another file.")

with tab2:
    st.info("📝 This demo uses a sample Odisha land sale deed document.")
    
    if st.button("🔍 Analyze Demo Document", type="primary"):
        with st.spinner("Analyzing..."):
            results = analyze_document(demo_text)
            
            st.success("✅ Document analyzed successfully!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Document Type", results['document_type'])
            with col2:
                score = results['overall_score']
                color = "🟢" if score >= 70 else "🟡" if score >= 40 else "🔴"
                st.metric("Legal Score", f"{color} {score:.0f}/100")
            
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📋 Extracted Information")
                if results['parties']:
                    st.write("**Parties Involved:**")
                    for p in results['parties']:
                        st.write(f"• {p}")
                if results['dates']:
                    st.write("**Dates Found:**")
                    for d in results['dates']:
                        st.write(f"• {d}")
                if results['amounts']:
                    st.write("**Amounts Found:**")
                    for a in results['amounts']:
                        st.write(f"• {a}")
                if results['plot_numbers']:
                    st.write("**Plot/Survey Numbers:**")
                    for p in results['plot_numbers']:
                        st.write(f"• {p}")
            
            with col2:
                st.subheader("✅ Compliance Check")
                for check, status in results['compliance'].items():
                    icon = "✅" if status else "❌"
                    st.write(f"{icon} {check}")
                
                st.subheader("⚠️ Red Flags")
                if results['red_flags']:
                    for flag in results['red_flags']:
                        st.warning(f"⚠️ {flag}")
                else:
                    st.success("✅ No red flags detected!")