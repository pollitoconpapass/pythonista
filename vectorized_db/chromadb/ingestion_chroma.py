import ollama
import chromadb
from time import sleep
from langchain.text_splitter import RecursiveCharacterTextSplitter

chroma_client = chromadb.PersistentClient(path="../chromadb") # -> it makes the collection created persists in your local env.


def generate_splitter(text: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = text_splitter.split_text(text)
    return chunks

def generate_embedding(text: str):
    response = ollama.embed(model="nomic-embed-text", input=text)
    embedding = response["embeddings"]
    return embedding


def generate_chromadb_index(text: str, index_name: str):
    collection = chroma_client.create_collection(name=index_name, 
                                                #  embedding_function=generate_embedding,
                                                 get_or_create=True)

    # Generate the chunks and embeddings
    chunks = generate_splitter(text)

    # Add the chunks to the collection
    for i, chunk in enumerate(chunks):
        embedding = generate_embedding(chunk)
        metadata = {
            "file_name": f"{index_name}.txt",
            "chunk_number": i + 1,
            "extracted_text": chunk
        }
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[f"chunk_{i+1}"]
        )

        sleep(1)

    print(f"Total embeddings generated: {len(chunks)} at Index: {index_name}")
    