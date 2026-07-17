import streamlit as st
import pandas as pd

st.title("📊 Career Dashboard")

st.metric("Resume Score", "82/100")
st.metric("Projects Suggested", "3")
st.metric("Certifications", "4")
st.metric("Skill Gap", "Medium")

skills = pd.DataFrame({
    "Category": ["Technical", "Soft", "Missing"],
    "Count": [8, 5, 4]
})

st.bar_chart(skills.set_index("Category"))

st.success("Keep learning consistently. You're making great progress!")