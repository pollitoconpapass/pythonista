import json
import requests

def llama3_llm(query):
    request = requests.post("http://localhost:11434/api/generate", 
                            json={"model": "llama3.1", "prompt": query})
    
    responses = [json.loads(line) for line in request.text.splitlines()]
    responses = [response["response"] for response in responses]
    answer = "".join(responses)

    return answer