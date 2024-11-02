'''FOR SPECIAL CASES (ex: TRANSLATION)'''

import os
import json
from dotenv import load_dotenv
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

load_dotenv('../../.env')

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_INDEX_NAME = "spa-quz-translation-index"
SRC_LANGUAGE_KEY= "spanish"
TGT_LANGUAGE_KEY = "cuzco quechua"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer(EMBEDDING_MODEL)
pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(PINECONE_INDEX_NAME)
initial_stats = index.describe_index_stats()
print(f"Initial index stats: {initial_stats}")

id = 0
with open('./words.json', 'r') as f:
    words = json.load(f)

    for word in words:
        source_sentence = word[SRC_LANGUAGE_KEY]
        target_sentence = word[TGT_LANGUAGE_KEY]
        source_sentence_embedding = model.encode(source_sentence).tolist()

        print(f"Source sentence: {source_sentence}")
        print(f"Target sentence: {target_sentence}")

        response = index.upsert(vectors=[(str(id), source_sentence_embedding, {"source_language": SRC_LANGUAGE_KEY, 
                                                              "source_sentence": source_sentence, 
                                                              "target_language": TGT_LANGUAGE_KEY, 
                                                              "target_sentence": target_sentence})])
        
        id+=1
        print(f"Upsert response for ID {id}: {response}")

print("Pinecone index created and populated successfully.")