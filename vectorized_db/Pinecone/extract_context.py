import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_INDEX_NAME = os.getenv('PINECONE_INDEX_NAME')

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)


def generate_embedding_from_text(text): # -> choose any embedding function you prefer
    pass


def retrieve_context(query: str):
    query_embedding = generate_embedding_from_text(query)

    response = index.query(
        vector=query_embedding,
        top_k=4,
        include_metadata=True
    )

    results = []
    for match in response:
        metadata = match['metadata']
        score = match['score']

        results.append({"metadata": metadata, "score": score})
        # If metadata contains important values, you can do so... "source_langauge": metadata["source_language"], ....

    return results