import os
from groq import Groq


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def groq_query(query):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="llama3-8b-8192",
        stream=False,  # Set this to True if you want to stream the response
    )

    return chat_completion.choices[0].message.content