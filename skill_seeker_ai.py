import streamlit as st
import openai
import requests


@st.cache_resource
def get_client():
    return openai.Client(api_key=st.secrets["OPENAI_API_KEY"])


def get_courses(skill):
    api_url = f"https://www.udemy.com/api-2.0/courses/?search={skill}"
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            courses = response.json().get("results", [])
            return [course['title'] for course in courses][:3]
    except requests.RequestException:
        pass
    return []


def get_ai_recommendation(user_input):
    client = get_client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that suggests the best skills to learn."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content


# Streamlit UI
st.title("🧠 Skill Seeker Lab AI")
st.subheader("Find the next skill you should learn!")

user_goal = st.text_input("What's your main learning goal? (e.g., career change, entrepreneurship, personal development)")
user_interest = st.text_input("What field or industry interests you the most?")
user_challenge = st.text_input("Any challenges you're facing? (e.g., lack of time, confidence, budget)")
user_budget = st.selectbox("What is your learning budget?", ["Free resources only", "$100 or less", "$500+", "No budget limit"])

if st.button("Get My Skill Recommendation"):
    ai_recommendation = get_ai_recommendation(
        f"Goal: {user_goal}, Interest: {user_interest}, Challenge: {user_challenge}, Budget: {user_budget}"
    )
    st.success(f"🎯 **AI-Powered Skill Recommendation:** {ai_recommendation}")

    courses = get_courses(user_interest)
    if courses:
        st.write("📚 **Recommended Courses:**")
        for course in courses:
            st.write(f"- {course}")
    else:
        st.write("No courses found. Try searching online learning platforms.")

st.write("💡 Stay curious and keep learning!")
