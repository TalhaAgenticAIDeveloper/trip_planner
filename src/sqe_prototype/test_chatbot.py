import litellm
from dotenv import load_dotenv
from crewai import LLM
import os

load_dotenv()


 





# def create_prompt_for_questions(project_title,project_requirements):
#     prompt = f"""
#         You are an AI assistant specializing in project analysis. Your task is to review the given project title and its existing requirements, then suggest **only the most important missing** features in the form of questions that ask about their addition.

#         ### **Instructions:**
#         - Carefully analyze the **project title** and **existing requirements**.
#         - Identify **3 to 5 critical missing features** that would improve the project.
#         - **Each missing feature must be framed as a question**, explicitly asking if it should be added.
#         - The questions must be **feature-focused**, practical, and essential for project success.
#         - Do **not** provide explanations or extra text—only the questions.

#         ### **Output Format:**
#         - The response should **only** contain 3 to 5 **clear, feature-related questions**.
#         - Ensure each question starts with phrases like:
#         - "Do you want to add..."
#         - "Would you like to include..."
#         - "Should the system have..."
#         - "Do you need support for..."
#         - "Would it be helpful to add..."

#         ### **Project Title:** {project_title}  
#         ### **Given Requirements:**  
#         {project_requirements}
#     """

#     return prompt


# def get_litellm_response(prompt):
#     response = litellm.completion(
#         model="gemini/gemini-2.0-flash-exp",  
#         api_key=os.getenv("GEMINI_API_KEY"),
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response['choices'][0]['message']['content']

# def main():
#     conversation_history = []
#     project_title = input("Enter the project title: ")
#     project_requirements = input("Enter the project requirements: ")

    
#     question_prompt = create_prompt_for_questions(project_title,project_requirements)
#     questions_response = get_litellm_response(question_prompt)
#     questions = questions_response.split("\n")
    
#     for index, question in enumerate(questions, start=1):
#         print(f"Question {index}: {question}")
#         user_answer = input("Your Answer: ")
#         conversation_history.append(f"Q: {question}\nA: {user_answer}")
    
#     print("\nInterview completed!")
#     print("### Conversation History:")
#     for convo in conversation_history:
#         print(convo)



import streamlit as st
import litellm
from dotenv import load_dotenv
import os

load_dotenv()

# Function to generate interview questions
def create_prompt_for_questions(user_domain):
    prompt = f"""
    You are an AI assistant specializing in interview preparation.
    Generate a list of 10 important interview questions for the domain: {user_domain}.
    Keep the questions clear, relevant, and suitable for an interview setting.
    """
    return prompt

# Function to get response from LiteLLM
def get_litellm_response(prompt):
    response = litellm.completion(
        model="gemini/gemini-2.0-flash-exp",  
        api_key=os.getenv("GEMINI_API_KEY"),
        messages=[{"role": "system", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "user_domain" not in st.session_state:
    st.session_state.user_domain = None

# UI for domain input
st.title("AI Interview Preparation Chat")
for index, question in enumerate(st.session_state.questions, start=st.session_state.current_question_index + 1):
    st.write(f"**Question {index}:** {question}")
    
    # Input box for user response
    user_answer = st.text_input("Your Answer:", key=f"answer_{index}")

    if st.button("Next Question", key=f"next_{index}"):
        if user_answer:
            # Store conversation history
            st.session_state.conversation_history.append(f"Q: {question}\nA: {user_answer}")
            st.session_state.current_question_index += 1
            st.experimental_rerun()
    
    break  # Ensures only one question is displayed at a time


# Display conversation history at the end
if st.session_state.current_question_index >= len(st.session_state.questions):
    st.success("Interview Completed!")
    st.subheader("### Conversation History:")
    for convo in st.session_state.conversation_history:
        st.write(convo)

