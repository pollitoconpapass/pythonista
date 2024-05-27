import soundfile as sf


audio_count = 0

def create_audio():
    # Some random process
    output = "some stuff"

    global audio_count
    audio_count += 1
    audio_file = f"audio_{audio_count}.wav"

    sf.write(audio_file, output.T, rate=16000, subtype="PCM_16", format="wav")

    # some extra process...