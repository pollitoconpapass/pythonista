import ollama

def generate_embedding(text):
    response = ollama.embed(model="nomic-embed-text", input=text)
    embedding = response["embeddings"]
    return embedding