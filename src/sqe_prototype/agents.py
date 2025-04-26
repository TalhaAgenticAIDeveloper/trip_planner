import os
from crewai import Agent
from crewai import LLM
from textwrap import dedent

from dotenv import load_dotenv
load_dotenv()

model = LLM(model="gemini/gemini-2.0-flash-exp" ,api_key="AIzaSyDlGuiJOqQePVsQEu5gWiftb74RDGvcq-c")

class TripAgents():
  

    def city_selection_agent(self):
        return Agent(
            role = 'City Selection Expert',
            goal = dedent('Select the best city based on weather, season, and prices'),
            backstory = dedent('An expert in analyzing travel data to pick ideal destinations'),
            tools=[],
            verbose = True,
            llm = model,
            )



    def local_expert(self):
        return Agent(
            role = 'Local Expert at this city',
            goal = dedent('Provide the BEST insights about the selected city'),
            backstory = dedent("""A knowledgeable local guide with extensive information
            about the city, it's attractions and customs"""),
            tools=[],
            verbose = True,
            llm = model,
            )

    def travel_concierge(self):
        return Agent(
            role = 'Amazing Travel Concierge',
            goal = dedent("""Create the most amazing travel itineraries with budget and 
            packing suggestions for the city"""),
            backstory = dedent("""Specialist in travel planning and logistics with 
            decades of experience"""),
            tools = [],
            verbose = True,
            llm = model,
            )