import streamlit as st
from backend.resume_parser import extract_text_from_pdf
from backend.chatbot import analyze_resume

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ Resume Uploaded Successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("🤖 AI is analyzing your resume..."):

        analysis = analyze_resume(resume_text)

    st.subheader("📊 AI Resume Analysis")

    st.markdown(analysis)