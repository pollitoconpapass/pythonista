import os
from groq import Groq


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def groq_query(query):
    stream = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        model="llama3-8b-8192",
        temperature=0.5,
        stream=True
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content, end="")