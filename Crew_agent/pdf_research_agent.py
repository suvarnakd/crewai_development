from crewai import Agent
# from Crew_agent.search_tool import pdftool
from crewai_tools import PDFSearchTool

# PDF_tool = PDFSearchTool()
# from langchain_community.llms import HuggingFaceHub

# llm = HuggingFaceHub(
#     repo_id="sentence-transformers/all-MiniLM-L6-v2",
#     huggingfacehub_api_token="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",
#     task="text-generation",
# )

# PDF_tool = PDFSearchTool( pdf='/home/pranjal/Desktop/crewai/transformer.pdf',
#     config=dict(
#         llm=dict(
#             provider="huggingface", # or google, openai, anthropic, llama2, ...
#             config=dict(
#                 model="sentence-transformers/all-MiniLM-L6-v2",
#                 temperature=0.7,
#                 top_p=2,
#                 stream=True,
#             ),
#         ),
#         embedder=dict(
#             provider="huggingface",
#             config=dict(
#                 model="sentence-transformers/all-MiniLM-L6-v2",
#                 # task_type="retrieval_document",
#                 # title="Embeddings",
#             ),
#         ),
#     )
# )
# print(PDF_tool)
PDF_tool = PDFSearchTool(pdf='transformer.pdf')

def pdf_reasercher(research):
    researcher = Agent(
        role='Senior Research Analyst',
        goal=research,
        backstory="""You work at a leading tech company.
        Your expertise lies in researching advanced machine learning models.
        You have a knack for dissecting complex data and presenting actionable insights.""",
        verbose=True,
        allow_delegation=False,
        tools=[PDF_tool]
        )
    return researcher