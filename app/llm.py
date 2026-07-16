from ollama import Client
from app.config import OLLAMA_HOST, OLLAMA_MODEL

client = Client(host=OLLAMA_HOST)


def chat_with_llm(prompt: str):
    response = client.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]