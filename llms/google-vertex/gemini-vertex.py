from google.oauth2.service_account import Credentials
from langchain_google_vertexai import ChatVertexAI

vertex_credentials = Credentials.from_service_account_file(
    "/Your/path/to/vertexAI-credentials.json"
)

vertex_llm = ChatVertexAI(
    model="gemini-2.0-flash-exp",
    credentials=vertex_credentials,
    project="qhali-inc",
    temperature=1.5,
    max_tokens=None,
    max_retries=6,
    stop=None,
)

def gemini_llm(sentence):
    messages = [
        ("system", '''You are a helpful AI assistant...'''),
        ("user", sentence)
    ]

    response = vertex_llm.invoke(messages)
    return response.content