'''
pip install pyngrok
'''

import uvicorn
from pyngrok import ngrok
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    # Start ngrok tunnel
    public_url = ngrok.connect(8000).public_url # -> make sure the PORT is the same as...
    print(f" * ngrok tunnel: {public_url}")

    # Run the FastAPI app with Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # -> ... this PORT 