import ollama

def chunk_analysis_4_translation(text: str):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "assistant", "content": "You are a helpful AI assistant"},
            {"role": "user", "content": text}
        ]
    )

    return response['message']['content']