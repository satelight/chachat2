from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import httpx

app = FastAPI()

OPENAI_API_KEY = "your-api-key-here"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"


class ChatRequest(BaseModel):
    message: str
    model: Optional[str] = "gpt-3.5-turbo"


@app.post("/chat")
async def chat(request: ChatRequest):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": request.model,
        "messages": [{"role": "user", "content": request.message}],
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(OPENAI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

    return {"response": result["choices"][0]["message"]["content"]}
