from flask import Flask, request
from jsonschema import validate


app = Flask(__name__)


@app.route("/", methods=["POST"])
def some_function():
    # some code 

    schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "env": {"type": "string", "enum": ["dev", "prod"]},  # -> enum is a list of the only possible values
        }
    }

    data = request.json()
    validate(instance=data, schema=schema)

    title = data.get("title")  # -> retrieve data from Postman
    env = data.get("env")

    print(f"The title selected is {title} and the env is {env}")

    # SOME OTHER CODE
