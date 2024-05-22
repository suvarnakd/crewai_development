import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from task import crewai_pdf_response, crewai_response



class InputText(BaseModel):
    text: str

# class InputText(BaseModel):
#     researcher_text: str
#     writer_text: str

crew_app = FastAPI()

@crew_app.get("/")
def read_root():
    return {"GENESIS": "Perception"}


@crew_app.post("/google_agent")
async def process_text(researcher_text: str, writer_text: str):
    try:
        result = crewai_response(researcher_text, writer_text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@crew_app.post("/pdf_agent")
async def process_text(researcher_text: str, writer_text: str):
    try:
        result = crewai_pdf_response(researcher_text, writer_text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    

