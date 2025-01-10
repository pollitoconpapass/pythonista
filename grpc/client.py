import grpc
from example_pb2 import TTSRequest, STTRequest
from example_pb2_grpc import SpeechRecognitionStub


def run_tts(text, region):
    channel = grpc.insecure_channel('localhost:50051')
    stub = SpeechRecognitionStub(channel)

    request = TTSRequest(text=text, region=region)  
    response = stub.tts(request)

    with open('output.wav', 'wb') as f:
        f.write(response.audio)

    print("Audio file saved to output.wav")


def run_stt():
    channel = grpc.insecure_channel('localhost:50051')
    stub = SpeechRecognitionStub(channel)

    with open("output.wav", 'rb') as f:
        audio_bytes = f.read()
        request = STTRequest(audio=audio_bytes)

    response = stub.stt(request)
    transcription = response.transcription
    print("Transcription: {}".format(transcription))


if __name__ == '__main__':
    run_tts("Mitan raymi chayamushkana wamrakuna. Kushikushpa shamuychina, tantallana tushuypachik. Tukuy piwan kaypinami riksinankunchina. Chaymantana kushikushpa, asikushpa kawsaypachik.", "cuzco")
    run_stt()