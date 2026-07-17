import streamlit as st
from backend.chatbot import career_chat

st.title("💬 AI Career Mentor")

question = st.text_area(
    "Ask anything about careers, placements, resumes, coding interviews, or learning..."
)

if st.button("Ask AI"):

    if question:

        with st.spinner("Thinking..."):

            answer = career_chat(question)

        st.markdown(answer)