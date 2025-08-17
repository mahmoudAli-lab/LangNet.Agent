from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from .service import LangAgent

app = FastAPI(title="LangNet.Agent - Python")
agent = LangAgent()

class AskRequest(BaseModel):
    query: str

@app.post('/ask')
async def ask(req: AskRequest):
    return agent.answer(req.query)

@app.post('/ingest')
async def ingest(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode(errors='ignore')
    agent.ingest_text(text, source=file.filename)
    return {"status": "ok", "filename": file.filename}
