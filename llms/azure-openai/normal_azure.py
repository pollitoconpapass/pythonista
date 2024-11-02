import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv("../../.env")

client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    api_version=os.getenv("AZURE_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_DEPLOYMENT")
)

def azure_llm(prompt):
    response = client.chat.completions.create(
        model="gpt4-o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content