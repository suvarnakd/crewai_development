from crewai import Agent
from langchain_community.llms import HuggingFaceHub



def writer(write):
  write = Agent(
    role='Content Writer',
    goal=write,
    backstory="""You are a renowned Content Writer, known for your compiling answers.
    You transform complex concepts into compelling narratives.""",
    verbose=True,
    allow_delegation=True,
  )
  return write
