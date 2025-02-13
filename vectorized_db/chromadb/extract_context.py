import ollama
import chromadb
from time import sleep
from langchain.text_splitter import RecursiveCharacterTextSplitter

chroma_client = chromadb.PersistentClient(path="../chromadb") 

def generate_embedding(text: str): # -> use the same embedding function as before
    pass

def extract_context_chromadb(question: str, index_name: str):
    collection = chroma_client.get_collection(name=index_name)
    if not collection:
        print(f"Collection {index_name} not found.")
        return ""

    query_embedding = generate_embedding(question)

    if not query_embedding:
        print("Error: Invalid embedding vector.")
        return ""

    try:
        context = collection.query(
            query_embeddings=[query_embedding],
            n_results=4,
        )
        formatted_context = context = [match.get('extracted_text', '') for match in context['metadatas'][0]]
        formatted_context = " ".join(formatted_context)

        print(f"Extracted context: {formatted_context}")

        return formatted_context

    except Exception as e:
        print(f"Error querying ChromaDB: {e}")
        print(f"Query embedding length: {len(query_embedding)}")
        print(f"First few values: {query_embedding[:2]}")
        return ""
    