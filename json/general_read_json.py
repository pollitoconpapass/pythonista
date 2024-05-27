import json


def read_json(file_path):
    with open(file_path, 'r') as f:
        json_data = json.load(f)

    return json_data

# You can use this like: 
json_data = read_json("config.json")
name = json_data.get("name")