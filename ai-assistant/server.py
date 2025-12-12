# server.py
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from assistant import handle_question

app = FastAPI(title="Rios AI API")

# CORS: libera acesso do front (Next.js em localhost:3000)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def root():
    return {"message": "Rios AI API is running"}


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    """
    Recebe uma mensagem do usuário e devolve a resposta do Rios AI.
    """
    answer = handle_question(req.message)
    return ChatResponse(reply=answer)
