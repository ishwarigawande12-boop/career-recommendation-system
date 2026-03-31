import streamlit as st
import matplotlib.pyplot as plt

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "login"

if "scores" not in st.session_state:
    st.session_state.scores = {
        "Analytical": 0,
        "Creative": 0,
        "Social": 0,
        "Leadership": 0
    }

# ---------------- LOGIN PAGE ----------------
def login_page():
    st.title("🔐 Login Page")

    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    password = st.text_input("Enter password", type="password")

    if st.button("Login"):
        if name and email and password:
            st.session_state.name = name
            st.session_state.page = "instructions"
        else:
            st.error("Please fill all fields")

# ---------------- INSTRUCTIONS PAGE ----------------
def instructions_page():
    st.title("📋 Instructions")

    st.write("""
    • Answer all questions honestly  
    • Choose the option that best matches you  
    • Click submit to see your personality analysis  
    """)

    if st.button("Start Test"):
        st.session_state.page = "questions"

# ---------------- QUESTIONS PAGE ----------------
def questions_page():
    st.title("🧠 Personality Test")

    questions = [
        ("Do you enjoy solving logical problems?", "Analytical"),
        ("Do you enjoy working with data or numbers?", "Analytical"),
        ("Do you like analyzing patterns?", "Analytical"),

        ("Do you enjoy drawing or designing?", "Creative"),
        ("Do you like writing or storytelling?", "Creative"),
        ("Do you enjoy music or artistic work?", "Creative"),

        ("Do you enjoy helping people?", "Social"),
        ("Do you like teamwork?", "Social"),

        ("Do you enjoy leading a team?", "Leadership"),
        ("Do you like organizing tasks?", "Leadership")
    ]

    answers = []

    for i, (q, _) in enumerate(questions):
        ans = st.radio(q, ["Yes", "Sometimes", "No"], key=i)
        answers.append(ans)

    def score(ans):
        return 2 if ans == "Yes" else 1 if ans == "Sometimes" else 0

    if st.button("Submit Test"):

        scores = {
            "Analytical": 0,
            "Creative": 0,
            "Social": 0,
            "Leadership": 0
        }

        for i, (_, category) in enumerate(questions):
            scores[category] += score(answers[i])

        st.session_state.scores = scores
        st.session_state.page = "result"

# ---------------- RESULT PAGE ----------------
def result_page():
    st.title("📊 Personality Analysis Result")

    scores = st.session_state.scores

    st.subheader(f"Hello {st.session_state.name} 👋")

    # SHOW SCORES
    for key, value in scores.items():
        st.write(f"{key}: {value}")

    # PERSONALITY TYPE
    st.subheader("🧠 Personality Type")

    dominant = max(scores, key=scores.get)

    st.success(f"You are {dominant} Type")

    # GRAPH
    st.subheader("📈 Personality Graph")

    labels = list(scores.keys())
    values = list(scores.values())

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Personality Analysis")

    st.pyplot(fig)

    # CAREER RECOMMENDATION
    st.subheader("💼 Career Recommendations")

    if dominant == "Analytical":
        st.write("• Software Developer")
        st.write("• Data Scientist")
        st.write("Reason: Strong logical and problem-solving skills")

    elif dominant == "Creative":
        st.write("• Graphic Designer")
        st.write("• UI/UX Designer")
        st.write("Reason: High creativity and imagination")

    elif dominant == "Social":
        st.write("• Psychologist")
        st.write("• Counselor")
        st.write("Reason: Good communication and helping nature")

    elif dominant == "Leadership":
        st.write("• Manager")
        st.write("• Entrepreneur")
        st.write("Reason: Strong leadership and decision-making skills")

    # FINAL MESSAGE
    st.subheader("📌 Final Suggestion")

    st.write("Choose a career that aligns with your personality, interests, and skills for long-term success.")

    if st.button("Restart"):
        st.session_state.page = "login"

# ---------------- PAGE ROUTING ----------------
if st.session_state.page == "login":
    login_page()

elif st.session_state.page == "instructions":
    instructions_page()

elif st.session_state.page == "questions":
    questions_page()

elif st.session_state.page == "result":
    result_page()