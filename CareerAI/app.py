import streamlit as st

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🎓",
    layout="wide"
)

# ---------------- HEADER ----------------

st.markdown("""
<h1 style='text-align:center;color:#4F46E5;'>
🎓 CareerPilot AI
</h1>

<h4 style='text-align:center;color:gray;'>
Your Intelligent AI Career Mentor Agent
</h4>
""", unsafe_allow_html=True)

st.divider()

# ---------------- HERO SECTION ----------------

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
### 🌍 SDG 4 – Quality Education

CareerPilot AI helps students discover the right career path using Artificial Intelligence.

### 🚀 What can it do?

✅ Analyze your Resume

✅ Identify Skill Gaps

✅ Generate Personalized Career Roadmaps

✅ Answer Career Questions

✅ Prepare for Placements & Interviews
""")

with col2:
    st.info("""
### 👨‍🎓 Target Users

• College Students

• Fresh Graduates

• Placement Aspirants

• Rural Students

• Career Switchers
""")

st.divider()

# ---------------- METRICS ----------------

st.subheader("📊 Project Highlights")

c1, c2, c3, c4 = st.columns(4)

c1.metric("AI Modules", "4")
c2.metric("Target SDG", "4")
c3.metric("Career Domains", "20+")
c4.metric("Free AI", "Groq")

st.divider()

# ---------------- FEATURES ----------------

st.subheader("✨ Features")

col1, col2 = st.columns(2)

with col1:

    st.success("""
📄 Resume Analyzer

Upload your resume and receive:
- Resume Score
- Strengths
- Weaknesses
- Certifications
""")

    st.info("""
🎯 Skill Gap Analyzer

Compare your skills with your dream job and discover what to learn next.
""")

with col2:

    st.warning("""
🗺 Career Roadmap Generator

Receive a personalized 30-60-90 day roadmap.
""")

    st.error("""
💬 AI Career Mentor

Ask career questions anytime and get AI-powered guidance.
""")

st.divider()

# ---------------- WORKFLOW ----------------

st.subheader("⚙️ How It Works")

st.markdown("""
```text
Upload Resume
        │
        ▼
AI Resume Analysis
        │
        ▼
Skill Gap Detection
        │
        ▼
Career Roadmap
        │
        ▼
AI Career Mentor Chat""")