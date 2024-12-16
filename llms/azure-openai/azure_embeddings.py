import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()


azure_client = AzureOpenAI(
    azure_endpoint =os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version = "2024-08-01-preview",
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_EMBEDDING")
)

def generate_embeddings(words: str): 
    response = azure_client.embeddings.create(model="text-embedding-ada-002", input=words)
    return response.data[0].embedding


# === MAIN ===
text = "What is the most common cause of heart failure?"
print(generate_embeddings(text))