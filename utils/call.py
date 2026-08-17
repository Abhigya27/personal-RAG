from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_chat(prompt,model="openai/gpt-oss-120b",temperature=0.3):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature, stream=True
    )

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            yield content