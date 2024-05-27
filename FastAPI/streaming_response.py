import io
import soundfile as sf
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


# === USING AUDIO FILES ===
@app.get("/audio")
async def make_some_process():
    # Some process
    output = "some_result"

    file_path = "path/to/file.mp3"
    sf.write(file_path, output.T, rate=16000, subtype="PCM_16", format="mp3")

    with open(file_path, "rb") as f:
        audio_bytes = f.read()

    return StreamingResponse(io.BytesIO(audio_bytes), media_type="audio/mp3")
