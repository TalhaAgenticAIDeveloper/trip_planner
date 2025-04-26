# from crewai import Agent , LLM
# from dotenv import load_dotenv
# import os
# load_dotenv()
# api_key=os.getenv("GEMINI_API_KEY")


# model = LLM(model="gemini/gemini-2.0-flash-exp" ,api_key=api_key)

# class Project_Manager_Agents:

    
#     ##################################################################################################
#     # Agent 1
#     ##################################################################################################
    

         

#     ##################################################################################################
#     # Agent 1
#     ##################################################################################################
#     def Project_Analysis_Agent(self):
#         return Agent(
#             role = "Project Planning Expert",

#             goal = """
#                     Analyze user-defined project requirements and determine the optimal team structure, including 
#                     the required roles, responsibilities, and workload distribution. Provide a well-structured foundation 
#                     for efficient project execution.
#                    """,

#             backstory= """
#                         A highly experienced project manager and strategist with 12+ years of expertise in software 
#                         development planning. Skilled in agile methodologies, team structuring, and resource allocation, ensuring 
#                         every project starts with a clear roadmap for success.
#                        """,

#             # verbose=True,
#             llm = model,
#             # allow_delegation=True,
            
#         )
    
#     ##################################################################################################
#     # Agent 2
#     ##################################################################################################

#     def Task_Breakdown_Agent(self):
#         return Agent(
#             role = "Project Workflow Architect",

#             goal = """
#                     Break down the project into well-defined tasks, assign responsibilities to each team member, 
#                     and establish a clear workflow. Ensure smooth task delegation, define dependencies, and estimate time 
#                     and cost for each phase of the project.
#                    """,

#             backstory= """
#                         A senior project architect with 10+ years of experience in task management, workflow optimization, 
#                         and team coordination. Expert in agile development, sprint planning, and process automation to ensure 
#                         efficiency and on-time delivery.
#                        """,

#             # verbose=True,
#             llm = model,
#             # allow_delegation=True,

#         )
    
#     #####################################################################################################
#     # Agent 3
#     #####################################################################################################

#     def Risk_Analysis_Agent(self):
#         return Agent(
#             role = "Risk Management Expert",

#             goal = """
#                     Identify potential risks in the project, including technical,
#                     financial, and operational challenges.Analyze the impact of each risk and provide 
#                     actionable mitigation strategies to ensure smooth project execution.
#                 """,

#             backstory= """
#                         A highly skilled risk analyst with over 12 years of experience in project risk assessment, contingency 
#                         planning, and crisis management. Expert in identifying vulnerabilities, assessing risk probability, and 
#                         implementing proactive solutions to minimize disruptions.
#                        """,

#             # verbose=True,
#             llm = model,
#             # allow_delegation=True,

#         )
#     ################################################################################################################
#     # Agent 4
#     ################################################################################################################

#     def Final_Report_Agent(self):
#         return Agent(
#             role = "Project Documentation Specialist",

#             goal = """
#                     Compile a comprehensive final report summarizing the project’s team structure, workflow, risk 
#                     assessment, timeline, and cost analysis. Ensure the report is clear, well-structured,
#                     and provides actionable insights.
#                    """,

#             backstory= """
#                          A seasoned technical writer and project analyst with over 10 years of experience in compiling 
#                          detailed project reports, business proposals, and post-mortem analyses. Expert in documentation, performance 
#                          evaluation, and delivering structured insights for decision-making.
#                         """,
            
#             # verbose=True,
#             llm = model,
#             # allow_delegation=True,

#         )





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