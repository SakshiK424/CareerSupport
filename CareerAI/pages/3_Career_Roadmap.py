import streamlit as st
from backend.chatbot import career_roadmap

st.title("🗺️ AI Career Roadmap")

role = st.text_input(
    "Dream Role",
    placeholder="Machine Learning Engineer"
)

company = st.text_input(
    "Dream Company",
    placeholder="Google"
)

if st.button("Generate Roadmap"):

    if role and company:

        with st.spinner("Generating your personalized roadmap..."):

            roadmap = career_roadmap(role, company)

        st.markdown(roadmap)