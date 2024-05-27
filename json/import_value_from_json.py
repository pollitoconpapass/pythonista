import os
import json

with open("config.json", "r") as f:
    data = json.load(f)

value = data.get("value")


# If the JSON is in other directory: 
ROOT_DIR = os.path.abspath(os.path.dirname(__file__), '..')  # -> consider using another '..' in case it is in another folder subdirectory
JSON_PATH = os.path.join(ROOT_DIR, 'folder_name', 'config.json')

with open(JSON_PATH, "r") as f:
    data = json.load(f)

value = data.get("value")