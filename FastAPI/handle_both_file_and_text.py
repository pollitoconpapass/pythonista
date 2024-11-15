from fastapi import FastAPI, File, Form, UploadFile


app = FastAPI()

@app.post("/ask-llama-vision")
async def answer(prompt: str = Form(...), file: UploadFile = File(...)):
    # Do something with the prompt and file
    return {"result": prompt}