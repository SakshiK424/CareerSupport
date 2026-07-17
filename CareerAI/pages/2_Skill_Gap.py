import streamlit as st
from backend.chatbot import skill_gap

st.title("🎯 Skill Gap Analyzer")

skills = st.text_area(
    "Enter your current skills",
    placeholder="Python, SQL, HTML..."
)

dream = st.text_input(
    "Dream Job",
    placeholder="AI Engineer"
)

if st.button("Analyze Skill Gap"):

    if skills and dream:

        with st.spinner("Analyzing..."):

            result = skill_gap(skills,dream)

        st.markdown(result)