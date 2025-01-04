import os
import requests
from dotenv import load_dotenv

load_dotenv()


medpalm_endpoint = os.getenv("MEDPALM_URL")
medpalm_api = os.getenv("MEDPALM_API_TOKEN")

headers = {
    "Content-Type": "application/json   charset=utf-8",
    "Authorization": f"Bearer {medpalm_api}"
}

def medpalm_llm(question: str):
    data = {
        "instances": [
            {
                "content": f'''Task: {question}'''
            }
        ],
        "parameters": {
            "temperature": 0,
            "maxOutputTokens": 500,
            "topK": 40,
            "topP": 0.95
        }
    }

    try:
        response = requests.post(medpalm_endpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["predictions"][0]["content"]
    
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        return None