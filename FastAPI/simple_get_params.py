from fastapi import FastAPI

app = FastAPI()


@app.get("/items")
async def read_item(text: str, language: str):
    return {"text": text, "language": language}


# In Postman -> http://127.0.0.1:8000/items?text=hello&language=es
    