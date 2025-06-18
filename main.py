from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = "sk-YourAPIKey"

class GPTRequest(BaseModel):
    input: str

@app.post("/gpt4")
async def gpt4(req: GPTRequest):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": req.input}]
    )
    return {"output": response['choices'][0]['message']['content']}