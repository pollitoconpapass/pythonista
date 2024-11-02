import os
import PyPDF2
import ollama
from pinecone import Pinecone
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv(dotenv_path='../../.env')

BATCH_SIZE = 100

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            num_pages = len(pdf_reader.pages)
            text = []
            
            for page in range(num_pages):
                page_obj = pdf_reader.pages[page]
                page_text = page_obj.extract_text()
                if page_text:
                    text.append(page_text)
                else:
                    print(f"Unable to extract text from page {page + 1} of {file_path}.")
            print(f"Text extracted from {num_pages} pages")
        return text 
    except Exception as e:
        print(f"Error when trying to open the file {file_path}: {e}")
        return []

def generate_embedding_from_text(text):
    response = ollama.embed(model="nomic-embed-text", input=text)
    embedding = response["embeddings"]
    return embedding

def ingest_pinecone(folder_path):
    embeddings = []
    ids = []
    metadatas = []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  
        chunk_overlap=100 
    )

    for file_path in os.listdir(folder_path):
        text = extract_text_from_pdf(f'{folder_path}/' + file_path)
        full_text = " ".join(text)

        chunks = text_splitter.split_text(full_text)

        for i, chunk in enumerate(chunks):
            embedding = generate_embedding_from_text(chunk) 

            if isinstance(embedding, list):
                flat_embedding = embedding[0]
                embeddings.append(flat_embedding)
                ids.append(f"{file_path}_chunk_{i+1}") 
                
                metadata = {
                    "file_name": file_path,
                    "chunk_number": i + 1,
                    "extracted_text": chunk 
                }
                metadatas.append(metadata)
            else:
                print(f"Unexpected embedding format for file: {file_path} (chunk {i+1})")

    if embeddings:
        for i in range(0, len(embeddings), BATCH_SIZE):
            end_index = min(i + BATCH_SIZE, len(embeddings))
            batch_vectors_with_metadata = [
                (id_, embedding, metadata) 
                for id_, embedding, metadata in zip(ids[i:end_index], embeddings[i:end_index], metadatas[i:end_index])
            ]
            index.upsert(vectors=batch_vectors_with_metadata)

    print(f"Total embeddings generated: {len(embeddings)}")


# === MAIN ===
folder_path = './pdfs'
ingest_pinecone(folder_path)
    