import json


json_file_path = "config.json"
with open(json_file_path, "r") as f:
    json_data = json.load(f)

    for i in json_data["data"]: # -> data is the mother field
        text = i["text"]["spanish"]  # -> subfields of the mother field