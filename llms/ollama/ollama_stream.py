import ollama

def llama3_stream(query):
    stream = ollama.chat(
        model="llama3.1",
        messages=[
            {"role": "assistant", "content": "You are a helpful assistant"},
            {"role": "user", "content": query}
        ],
        stream=True
    )

    for chunk in stream:
        print(chunk['message']['content'], end="", flush=True)