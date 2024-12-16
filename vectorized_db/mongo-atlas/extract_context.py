import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# === GENERAL CONFIG ====
MONGO_URL = os.getenv("MONGO_HOST")
MONGO_DB_NAME = os.getenv("MONGO_DATABASE_NAME")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

mongo_client = MongoClient(MONGO_URL, tlsCAFile=certifi.where())
db = mongo_client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

def embeddings(text: str):  # -> pick any embedding function of the model you want to use (OLLAMA, AZURE)
    pass

def retrieve_context(query: str, k: int = 10):
    query_embedding = embeddings(query)

    similar_docs = collection.aggregate([
        {
            "$vectorSearch": {
                "queryVector": query_embedding,
                "path": "embedding",
                "numCandidates": 10,
                "limit": k,
                "index": "default",
            }
        }
    ])

    results = []
    for doc in similar_docs:
        metadata = doc["metadata"]
        text = doc["text"]
        results.append({"metadata": metadata, "text": text})

    return results # -> keep in mind this will be a list of dictionaries