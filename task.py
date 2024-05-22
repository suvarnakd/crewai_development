from crewai import Agent, Task, Crew, Process
from Crew_agent.research_agent import researcher
from Crew_agent.pdf_research_agent import pdf_reasercher
from Crew_agent.writer_agent import writer



def crewai_response(research_task, write_task):
    print(research_task)
    print(write_task)
    task1 = Task(
    max_iter=5,
    description="""Conduct a comprehensive analysis""",
    expected_output= "Full analysis report in bullet points",
    agent=researcher(research_task)
    )

    task2 = Task(
    max_iter=5,
    description="""Using the insights provided, develop an engaging answer""",
    expected_output=  "Comprehensive answer",
    agent=writer(write_task)
    )

    crew = Crew(
    agents=[researcher(research_task), writer(write_task)],
    tasks=[task1, task2],
    verbose=2, 
    )

    result = crew.kickoff()
    print(result)
    return result


def crewai_pdf_response(research_task, write_task):
    print(research_task)
    print(write_task)
    task1 = Task(
    max_iter=2,
    description="""Conduct a comprehensive analysis. Identify the exact and accuracte answers""",
    expected_output= "Full analysis report in bullet points",
    agent=pdf_reasercher(research_task)
    )

    task2 = Task(
    max_iter=2,
    description="""Using the insights provided, develop an engaging answer.""",
    expected_output=  "An exact comprehensive answer",
    agent=writer(write_task)
    )

    crew = Crew(
    agents=[pdf_reasercher(research_task), writer(write_task)],
    tasks=[task1, task2],
    verbose=2, 
    )

    result = crew.kickoff()
    print(result)
    return result
