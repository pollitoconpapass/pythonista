import os
from dotenv import load_dotenv


load_dotenv()  # -> if your .env is in other directory ... load_dotenv("path/to/.env")
name = os.getenv("NAME")