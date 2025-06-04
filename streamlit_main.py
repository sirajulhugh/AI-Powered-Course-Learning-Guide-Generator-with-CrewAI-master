# SQLite fix for ChromaDB - MUST be at the very top
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


import streamlit as st
from datetime import datetime
from course_planner.crew import CoursePlanner
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Streamlit app
def run_streamlit_app():
    st.title("🎓 AI Course Learning Guide Generator")
    st.write("Generate a personalized learning plan for any technical course or technology!")

    with st.form("learning_guide_form"):
        course_name = st.text_input("Course Name", placeholder="e.g., Node.js, React, Python")
        duration = st.text_input("Learning Duration", placeholder="e.g., 3 months, 6 weeks, 1 year")
        skill_level = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced"])
        daily_hours = st.number_input("Daily Hours", min_value=1, max_value=24, value=2, step=1)
        learning_style = st.selectbox("Learning Style", ["Visual", "Hands-On", "Reading", "Mixed"])
        career_goal = st.text_input("Career Goal", placeholder="e.g., Web Developer, Data Scientist")

        submitted = st.form_submit_button("Generate Learning Guide")

    if submitted:
        inputs = {
            "course_name": course_name,
            "duration": duration,
            "skill_level": skill_level.lower(),
            "daily_hours": daily_hours,
            "learning_style": learning_style.lower(),
            "career_goal": career_goal,
            "current_date": f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}",
        }

        st.info("🚀 Generating comprehensive learning guide...")
        try:
            result = CoursePlanner().crew().kickoff(inputs=inputs)
            st.success("✅ Learning guide generated successfully!")

            # Display generated files
            st.subheader("📁 Generated Outputs")
            output_files = [
                "prerequisites.md",
                "curriculum.md",
                "timeline.md",
                "resources.md",
                "projects.md",
                "study_strategy.md",
                "assessments.md",
                "communities.md",
                "certifications.md",
                "career_pathway.md",
            ]
            for file_name in output_files:
                file_path = f"output/{file_name}"
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as file:
                        st.markdown(f"### {file_name.replace('.md', '').capitalize()}")
                        st.markdown(file.read())

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    run_streamlit_app()
