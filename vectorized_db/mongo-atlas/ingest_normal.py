import os
import time
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_openai import AzureOpenAIEmbeddings
from concurrent.futures import ThreadPoolExecutor, as_completed
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

load_dotenv()

# === GENERAL DATA ===
start = time.time()
URL = os.getenv("MONGO_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = MongoClient(URL)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_DEPLOYMENT"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    api_key=os.getenv("AZURE_API_KEY"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT")
)


# === EMBEDDING FUNCTION ===
def process_document(doc):
    embedding = embeddings.embed_query(doc.page_content)
    return {
        "text": doc.page_content,
        "metadata": {
            "source": os.getenv("SPECIALTY_NAME"), # -> change it in the .env for your specialty name
        },
        "embedding": embedding
    }

# === LOADING DATA ===
PDF_DIR = os.getenv("PDF_DIR")
loader = DirectoryLoader(PDF_DIR, glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# === INITALIZING MONGO ATLAS ===
batch_size = 100
current_size = 0
processed_docs = []

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_document, doc) for doc in texts]
    total_size = len(texts)
    for future in as_completed(futures):
        processed_docs.append(future.result())

        if len(processed_docs) >= batch_size:
            current_size += batch_size
            collection.insert_many(processed_docs)
            print(f"Inserted {current_size} of {total_size} documents")
            processed_docs = []

if processed_docs:
    current_size += batch_size
    collection.insert_many(processed_docs)
    print(f"Inserted {current_size} of {total_size} documents")

print(f"Vector DB Successfully Created! Took {time.time() - start} seconds")