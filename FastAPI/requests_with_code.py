import requests


url = "http://127.0.0.1:8000/"
req_data = {
    "question": "what is your name?",
    "newThread": False
}

request_1 = requests.post(url, json=req_data)

if request_1.status_code == 200:
    # To collect specific values from the response
    collection_id = request_1.json().get("collection_id") # or ... collection_id = request_1.json()["collection_id"]

else: 
    print("Error: ", request_1.text)