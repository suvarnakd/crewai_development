from crewai import Agent
from Crew_agent.search_tool import google_search
# from langchain_community.llms import HuggingFaceHub

# llm = HuggingFaceHub(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.2",
#     huggingfacehub_api_token="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",
#     task="text-generation",
# )

def researcher(research):
  research = Agent(
    role='Senior Research Analyst',
    goal=research,
    backstory="""You work at a leading tech. Your expertise lies in researching 
    and getting the most relevant data.""",
    verbose=True,
    allow_delegation=False,
    tools=[google_search()]
  )
  return research
