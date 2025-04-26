from agents import TripAgents
from tasks import TripTasks
from crewai import Crew
import litellm
import streamlit as st
import markdown


import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")






st.title("🌍 Trip Planner Crew")
st.markdown("Plan your perfect trip with the help of specialized agents.")


origin = st.text_input("From where will you be traveling?")
cities = st.text_area("What are the cities you’re interested in visiting?")
date_range = st.text_input("What is the date range for your trip?")
interests = st.text_area("List your high-level interests and hobbies.")
# submitted = st.form_submit_button("Plan My Trip")



############################################################################################
# Creating Agents and Tasks
############################################################################################


agents = TripAgents()
tasks = TripTasks()

city_selector_agent = agents.city_selection_agent()
local_expert_agent = agents.local_expert()
travel_concierge_agent = agents.travel_concierge()



# Assigning Tasks
identify_task = tasks.identify_task(
            city_selector_agent,
            origin,
            cities,
            interests,
            date_range
        )
gather_task = tasks.gather_task(
            local_expert_agent,
            origin,
            interests,
            date_range
        )
plan_task = tasks.plan_task(
            travel_concierge_agent,
            origin,
            interests,
            date_range
        )
############################################################################################
# Creating Crew
############################################################################################

crew = Crew(
            agents=[city_selector_agent, local_expert_agent, travel_concierge_agent],
            tasks=[identify_task, gather_task, plan_task],
            verbose=True
        )


# def save_output_to_markdown(output, filename="agent_output.md"):
#     """Saves the output in a structured Markdown file."""
#     with open(filename, "w", encoding="utf-8") as file:
#         file.write(output.replace("**", ""))

if st.button("Submit"):
    with st.spinner("Processing... Please wait"):
        results = crew.kickoff()
        output_text = results.raw 
        st.markdown(output_text)
      
       
        
