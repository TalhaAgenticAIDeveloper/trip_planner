# from crewai import  Task
# from crewai_tools import SerperDevTool
# from dotenv import load_dotenv
# import os 
# load_dotenv()


# os.getenv("GEMINI_API_KEY")

# research_tool = SerperDevTool()

# class Project_Manager_Tasks():

# ##############################################################################################################
#     # Task 1
# ##############################################################################################################
    
#     def Project_Analysis_Task(self, agent, project_Title, Project_Requirements, further_context):
#         return Task(
#             description=f"""Analyze the user-defined project '{project_Title}' by reviewing its initial and enhanced requirements. 

#             The agent will:
#             - Evaluate the given project requirements: {Project_Requirements}
#             - Incorporate additional enhancements from previous analysis: {further_context}
#             - Determine the necessary team structure and skill sets required.

#             Parameters:
#             - Project Title: {project_Title}
#             - Initial Requirements: {Project_Requirements}
#             - Enhanced Requirements from previous analysis: {further_context}

#             The agent will analyze the complexity and scope of the project, 
#             identify the required team roles (frontend developers, backend developers, UI/UX designers, testers, project managers, etc.), 
#             and estimate the ideal team size.
#             """,
            
#             tools=[],
#             agent=agent,
#             expected_output="A structured report detailing the required team composition, skill set, and estimated team size."
#     )


# ##############################################################################################################
#     # Task 2
# ##############################################################################################################
 
#     def Task_Breakdown_Task(self, agent, context):
#         return Task(
#             description=f"""Break down the project into specific tasks based on the provided team structure.
#                 The agent will define the sequence of tasks, assign responsibilities to each team member, and create a task 
#                 dependency flowchart.
#                 """,
#             context = context,
#             tools = [research_tool],  # Fetch real-time cost and time estimates
#             agent = agent,
#             expected_output = "A detailed work breakdown structure (WBS) with task dependencies, estimated time, and assigned roles."
#     )



# ##############################################################################################################
#     # Task 3
# ##############################################################################################################

#     def Risk_Analysis_Task(self, agent, context):
#         return Task(
#             description = f"""Perform a risk analysis for the project based on the provided work breakdown structure.
            
#                 Context from previous agent:
#                 {context}

#                 The agent will identify risks related to time delays, resource shortages, technology limitations, and 
#                 budget overruns, and suggest mitigation strategies.
#                 """,
#             context = context,
#             tools = [research_tool],  # Fetch real-world risk data
#             agent = agent,
#             expected_output = "A comprehensive risk assessment report detailing all possible risks and their mitigation strategies."
#     )



# ##############################################################################################################
#     # Task 4
# ##############################################################################################################

#     def Final_Report_Task(self, agent, context):
#         return Task(
#             description = f"""Compile the final project report summarizing all aspects, including team composition, work 
#                 breakdown, risk analysis, and cost evaluation.
                
#                 Context from previous agent:
#                 {context}

#                 The agent will structure the final report with all necessary sections, ensuring clarity and completeness.
#                 """,

#             context = context,
#             tools = [],
#             agent = agent,
#             expected_output = "A professionally formatted final project report covering all essential project insights."
#     )



from crewai import Task
from textwrap import dedent


class TripTasks:

    def identify_task(self, agent, origin, cities, interests, range_date):
        return Task(
            description = dedent(f"""
                Analyze and select the best city for the trip based 
                on specific criteria such as weather patterns, seasonal
                events, and travel costs. This task involves comparing
                multiple cities, considering factors like current weather
                conditions, upcoming cultural or seasonal events, and
                overall travel expenses. 
                
                Your final answer must be a detailed
                report on the chosen city, and everything you found out
                about it, including the actual flight costs, weather 
                forecast and attractions.
                {self.__tip_section()}

                Traveling from: {origin}
                City Options: {cities}
                Trip Date: {range_date}
                Traveler Interests: {interests}
            """),
            agent = agent,
            expected_output = "Detailed report on the chosen city including flight costs, weather forecast, and attractions"
        )

    def gather_task(self, agent, origin, interests, range_date):
        return Task(
            description = dedent(f"""
                As a local expert on this city you must compile an 
                in-depth guide for someone traveling there and wanting 
                to have THE BEST trip ever!
                Gather information about key attractions, local customs,
                special events, and daily activity recommendations.
                Find the best spots to go to, the kind of place only a
                local would know.
                This guide should provide a thorough overview of what 
                the city has to offer, including hidden gems, cultural
                hotspots, must-visit landmarks, weather forecasts, and
                high level costs.
                
                The final answer must be a comprehensive city guide, 
                rich in cultural insights and practical tips, 
                tailored to enhance the travel experience.
                {self.__tip_section()}

                Trip Date: {range_date}
                Traveling from: {origin}
                Traveler Interests: {interests}
            """),
            agent = agent,
            expected_output = "Comprehensive city guide including hidden gems, cultural hotspots, and practical travel tips"
        )

    def plan_task(self, agent, origin, interests, range_date):
        return Task(
            description = dedent(f"""
                Expand this guide into a full 7-day travel 
                itinerary with detailed per-day plans, including 
                weather forecasts, places to eat, packing suggestions, 
                and a budget breakdown.
                
                You MUST suggest actual places to visit, actual hotels 
                to stay and actual restaurants to go to.
                
                This itinerary should cover all aspects of the trip, 
                from arrival to departure, integrating the city guide
                information with practical travel logistics.
                
                Your final answer MUST be a complete expanded travel plan,
                formatted as markdown, encompassing a daily schedule,
                anticipated weather conditions, recommended clothing and
                items to pack, and a detailed budget, ensuring THE BEST
                TRIP EVER. Be specific and give it a reason why you picked
                each place, what makes them special! {self.__tip_section()}

                Trip Date: {range_date}
                Traveling from: {origin}
                Traveler Interests: {interests}
            """),
            agent = agent,
            expected_output = "Complete expanded travel plan with daily schedule, weather conditions, packing suggestions, and budget breakdown"
        )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $1000!"