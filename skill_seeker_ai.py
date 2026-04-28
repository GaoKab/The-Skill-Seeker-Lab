import streamlit as st
import requests

SKILL_DATABASE = {
    "technology": {
        "skills": ["Python Programming", "Web Development", "Data Analysis", "Cloud Computing", "Cybersecurity"],
        "career_change": "Python Programming is the most versatile entry point into tech. It's beginner-friendly and opens doors to web dev, data science, automation, and AI.",
        "entrepreneurship": "Web Development (HTML/CSS/JavaScript) lets you build and launch your own products without hiring developers.",
        "personal development": "Data Analysis with Python or Excel helps you make better decisions in any area of life and career.",
    },
    "business": {
        "skills": ["Digital Marketing", "Financial Literacy", "Project Management", "Sales & Negotiation", "Business Analytics"],
        "career_change": "Digital Marketing is in high demand and has a low barrier to entry. Start with Google Analytics and social media marketing.",
        "entrepreneurship": "Financial Literacy is essential. Learn accounting basics, cash flow management, and how to read financial statements.",
        "personal development": "Project Management (try PMP or Agile/Scrum) teaches you to organize any complex goal into achievable steps.",
    },
    "creative": {
        "skills": ["Graphic Design", "Video Editing", "UX/UI Design", "Content Writing", "Photography"],
        "career_change": "UX/UI Design combines creativity with tech and has strong job demand. Start with Figma — it's free.",
        "entrepreneurship": "Content Writing and copywriting let you market anything. Every business needs someone who can write compelling copy.",
        "personal development": "Graphic Design with tools like Canva or Figma lets you express ideas visually and is useful in almost any role.",
    },
    "healthcare": {
        "skills": ["First Aid & CPR", "Health Informatics", "Nutrition Science", "Mental Health Awareness", "Medical Coding"],
        "career_change": "Medical Coding and Health Informatics are growing fields that don't require a medical degree to enter.",
        "entrepreneurship": "Nutrition Science or wellness coaching lets you build a personal brand and help others at the same time.",
        "personal development": "Mental Health Awareness and mindfulness practices improve every aspect of your personal and professional life.",
    },
    "finance": {
        "skills": ["Personal Investing", "Accounting Fundamentals", "Cryptocurrency Basics", "Financial Planning", "Excel for Finance"],
        "career_change": "Accounting Fundamentals and Excel are the gateway into finance roles. Consider pursuing a bookkeeping certification.",
        "entrepreneurship": "Personal Investing knowledge helps you grow wealth and understand the financial side of running a business.",
        "personal development": "Financial Planning teaches you to budget, save, and plan for the future with confidence.",
    },
    "education": {
        "skills": ["Public Speaking", "Curriculum Design", "Online Teaching", "Educational Technology", "Tutoring"],
        "career_change": "Online Teaching is booming. Platforms like Udemy and Coursera let you teach what you know to a global audience.",
        "entrepreneurship": "Curriculum Design lets you create and sell courses. Pair it with digital marketing to build an education business.",
        "personal development": "Public Speaking builds confidence and leadership skills that transfer to every area of life.",
    },
    "dance": {
        "skills": ["Choreography", "Dance Fitness Instruction", "Movement Therapy", "Stage Performance", "Dance Video Production"],
        "career_change": "Dance Fitness Instruction (Zumba, Barre) has low certification costs and growing demand in gyms and online.",
        "entrepreneurship": "Dance Video Production lets you build a YouTube/TikTok brand. Combine dance skills with basic video editing.",
        "personal development": "Choreography develops creativity, discipline, and body awareness. Start by learning different dance styles.",
    },
}

DEFAULT_SKILLS = {
    "skills": ["Communication Skills", "Time Management", "Critical Thinking", "Basic Coding", "Financial Literacy"],
    "career_change": "Communication Skills (writing, presenting, negotiating) are universally valued across every industry.",
    "entrepreneurship": "Basic Coding gives you the power to prototype ideas, automate tasks, and understand technology decisions.",
    "personal development": "Critical Thinking helps you evaluate information, solve problems, and make better decisions in all areas of life.",
}

BUDGET_TIPS = {
    "Free resources only": "Check out free platforms: YouTube tutorials, Khan Academy, freeCodeCamp, Coursera (audit mode), and MIT OpenCourseWare.",
    "$100 or less": "Great budget! Look at Udemy sales ($10-15 courses), Skillshare free trials, and affordable certifications on Coursera.",
    "$500+": "Consider structured programs: Coursera Professional Certificates, LinkedIn Learning annual plans, or community college courses.",
    "No budget limit": "Invest in top-tier options: university bootcamps, professional certifications (PMP, AWS, Google), or 1-on-1 coaching.",
}

CHALLENGE_TIPS = {
    "time": "Try microlearning: 15-20 minutes daily beats long weekend sessions. Apps like Duolingo and Brilliant use this approach.",
    "confidence": "Start with beginner-friendly platforms that have built-in communities (freeCodeCamp, Codecademy). Small wins build momentum.",
    "budget": "Many top skills can be learned for free. YouTube, library books, and open-source communities are underrated resources.",
    "motivation": "Set a 30-day challenge with a specific, visible goal (build a website, complete a course). Track streaks to stay accountable.",
}


def get_recommendation(goal, interest, challenge, budget):
    interest_lower = interest.lower().strip()
    goal_lower = goal.lower().strip()

    match = None
    for category, data in SKILL_DATABASE.items():
        if category in interest_lower or interest_lower in category:
            match = data
            break
        for skill in data["skills"]:
            if interest_lower in skill.lower():
                match = data
                break
        if match:
            break

    if not match:
        match = DEFAULT_SKILLS

    goal_key = "personal development"
    for key in ["career_change", "entrepreneurship", "personal development"]:
        if key.replace("_", " ") in goal_lower or key.replace("_", "") in goal_lower:
            goal_key = key
            break
    if "career" in goal_lower:
        goal_key = "career_change"
    elif "business" in goal_lower or "entrepreneur" in goal_lower or "startup" in goal_lower:
        goal_key = "entrepreneurship"

    recommendation = match[goal_key]
    top_skills = match["skills"]

    challenge_tip = None
    if challenge:
        challenge_lower = challenge.lower()
        for keyword, tip in CHALLENGE_TIPS.items():
            if keyword in challenge_lower:
                challenge_tip = tip
                break

    budget_tip = BUDGET_TIPS.get(budget, "")

    return recommendation, top_skills, challenge_tip, budget_tip


def get_courses(skill):
    try:
        api_url = f"https://www.udemy.com/api-2.0/courses/?search={skill}"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            courses = response.json().get("results", [])
            return [course["title"] for course in courses][:3]
    except requests.RequestException:
        pass
    return []


# Streamlit UI
st.title("Skill Seeker Lab AI")
st.subheader("Find the next skill you should learn!")

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

if st.button("Get My Skill Recommendation"):
    if not user_goal and not user_interest:
        st.warning("Please fill in at least your learning goal or field of interest.")
    else:
        recommendation, top_skills, challenge_tip, budget_tip = get_recommendation(
            user_goal, user_interest, user_challenge, user_budget
        )

        st.success(f"**Recommended Focus:** {recommendation}")

        st.write("**Top Skills in This Area:**")
        for skill in top_skills:
            st.write(f"- {skill}")

        if challenge_tip:
            st.info(f"**Tip for your challenge:** {challenge_tip}")

        if budget_tip:
            st.write(f"**Budget tip:** {budget_tip}")

        courses = get_courses(user_interest)
        if courses:
            st.write("**Recommended Courses:**")
            for course in courses:
                st.write(f"- {course}")

st.write("Stay curious and keep learning!")
