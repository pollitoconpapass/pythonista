import gc
import os
import time
import logging
from functools import wraps
from openai import AzureOpenAI
from pymongo import MongoClient
from requests.exceptions import HTTPError, Timeout
from langchain_community.document_loaders import PyPDFLoader
from concurrent.futures import ThreadPoolExecutor, as_completed
from langchain.text_splitter import RecursiveCharacterTextSplitter


logging.basicConfig(level=logging.INFO)

# === GENERAL DATA ===
start = time.time()
URL = os.getenv("MONGO_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = MongoClient(URL)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

azure_endpoint = os.getenv("AZURE_ENDPOINT")
api_key = os.getenv("AZURE_API_KEY")
api_version = os.getenv("OPENAI_API_VERSION")
deployment_name = os.getenv("AZURE_DEPLOYMENT")

azure_client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=azure_endpoint
)

# === RETRY DECORATOR ===
def retry(ExceptionToCheck, tries=4, delay=3, backoff=2):
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = f"{str(e)}, Retrying in {mdelay} seconds..."
                    logging.warning(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)
        return f_retry
    return deco_retry

# === EMBEDDING FUNCTION ===
@retry((HTTPError, Timeout), tries=4, delay=3, backoff=2)
def process_document(doc):
    embedding = azure_client.embeddings.create(input=[doc.page_content], model=deployment_name).data[0].embedding
    return {
        "text": doc.page_content,
        "metadata": {
            "source": os.getenv("SPECIALTY_NAME"),
        },
        "embedding": embedding
    }

# === PROCESSING IN BATCHES ===
batch_size = 1000  # Insertar en MongoDB cada 1000 embeddings
num_workers = os.cpu_count() // 3  # Definir cantidad de workers a la mitad de los núcleos disponibles

def process_batch(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(docs)
    processed_docs = [] 

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(process_document, doc) for doc in texts]
        for future in as_completed(futures):
            try:
                processed_docs.append(future.result())
                if len(processed_docs) >= batch_size:
                    collection.insert_many(processed_docs)
                    print(f"Inserted {len(processed_docs)} documents")
                    processed_docs = []
                    gc.collect()
            except Exception as e:
                logging.error(f"Error processing document: {e}")

    if processed_docs:
        collection.insert_many(processed_docs)
        print(f"Inserted the final {len(processed_docs)} documents")
        del processed_docs
        gc.collect()


# === MAIN ===
PDF_DIR = os.getenv("PDF_DIR")
pdf_files = [os.path.join(PDF_DIR, f) for f in os.listdir(PDF_DIR) if f.endswith('.pdf')]
print(f"Processing {len(pdf_files)} PDF files...")

for pdf_file in pdf_files:
    pdf_loader = PyPDFLoader(pdf_file)
    print(f"Processing PDF file: {pdf_file}")
    documents = pdf_loader.load()

    print(f"Loaded {len(documents)} documents from PDF file")
    process_batch(documents)

print(f"Vector DB Successfully Created! Took {time.time() - start} seconds")