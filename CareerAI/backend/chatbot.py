import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_ai(prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":"You are an expert AI Career Mentor helping students with careers, resumes, placements and interview preparation."
            },
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.5,
        max_tokens=1200
    )

    return response.choices[0].message.content


def analyze_resume(text):

    prompt=f"""
Analyze this resume.

Return:

Resume Score (/100)

Technical Skills

Soft Skills

Strengths

Weaknesses

Missing Skills

Recommended Certifications

Suggested Projects

Career Recommendation

Resume:

{text}
"""

    return ask_ai(prompt)


def skill_gap(skills,dream_job):

    prompt=f"""
Current Skills:

{skills}

Dream Job:

{dream_job}

Tell me:

1 Missing Skills

2 Learning Priority

3 Recommended Courses

4 Estimated Learning Time

5 Final Advice
"""

    return ask_ai(prompt)


def career_roadmap(role,company):

    prompt=f"""
Create a detailed roadmap.

Dream Role:
{role}

Dream Company:
{company}

Return:

30 Day Plan

60 Day Plan

90 Day Plan

Projects

Certifications

Interview Preparation Tips
"""

    return ask_ai(prompt)


def career_chat(question):

    return ask_ai(question)