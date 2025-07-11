from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import json

OPENAI_API_KEY = "your-api-key-here"

OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

app = FastAPI()

# CORS設定（このコードをFastAPIインスタンス作成直後に追加）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Svelteの開発サーバーURL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    model: Optional[str] = "gpt-3.5-turbo"


async def openai_stream(message: str, model: str | None):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": message}],
        "stream": True,
    }

    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream(
            "POST", OPENAI_API_URL, headers=headers, json=payload
        ) as response:
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    data = line[len("data: ") :]
                    if data.strip() == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        content = chunk["choices"][0]["delta"].get("content")
                        if content:
                            yield content
                    except json.JSONDecodeError:
                        continue


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.post("/chat")
async def chat(request: ChatRequest):
    print(request.message, request.model)
    response = StreamingResponse(
        openai_stream(request.message, request.model), media_type="text/plain"
    )
    print(response)
    return response
