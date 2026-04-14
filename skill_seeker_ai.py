import streamlit as st
import openai
import requests

# Set up OpenAI API key from Streamlit secrets or environment
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except (FileNotFoundError, KeyError):
    import os
    api_key = os.environ.get("OPENAI_API_KEY", "")

client = openai.Client(api_key=api_key) if api_key else None


# Function to fetch real-time course recommendations
def get_courses(skill):
    api_url = f"https://www.udemy.com/api-2.0/courses/?search={skill}"
    response = requests.get(api_url)
    if response.status_code == 200:
        courses = response.json().get("results", [])
        return [course["title"] for course in courses][:3]
    return []


# Function to generate AI-based skill recommendation
def get_ai_recommendation(user_input):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that suggests the best skills to learn.",
            },
            {"role": "user", "content": user_input},
        ],
    )
    return response.choices[0].message.content


# Streamlit UI
st.title("Skill Seeker Lab AI")
st.subheader("Find the next skill you should learn!")

# User input section
user_goal = st.text_input(
    "What's your main learning goal? (e.g., career change, entrepreneurship, personal development)"
)
user_interest = st.text_input(
    "What field or industry interests you the most?"
)
user_challenge = st.text_input(
    "Any challenges you're facing? (e.g., lack of time, confidence, budget)"
)
user_budget = st.selectbox(
    "What is your learning budget?",
    ["Free resources only", "$100 or less", "$500+", "No budget limit"],
)

# AI-generated recommendation
if st.button("Get My Skill Recommendation"):
    if not client:
        st.error("OpenAI API key not configured. Add it to `.streamlit/secrets.toml` or set the OPENAI_API_KEY environment variable.")
    else:
        ai_recommendation = get_ai_recommendation(
            f"Goal: {user_goal}, Interest: {user_interest}, Challenge: {user_challenge}"
        )
        st.success(f"**AI-Powered Skill Recommendation:** {ai_recommendation}")

    # Fetch real-time courses
    courses = get_courses(user_interest)
    if courses:
        st.write("**Recommended Courses:**")
        for course in courses:
            st.write(f"- {course}")
    else:
        st.write("No courses found. Try searching online learning platforms.")

st.write("Stay curious and keep learning!")
