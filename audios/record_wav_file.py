import speech_recognition


def wav_record(): 
    r = speech_recognition.Recognizer()

    while True:
        print("Recording... Press Enter to stop")

        with speech_recognition.Microphone() as source:
            audio = r.listen(source)


        # TO PRINT WHAT YOU'VE SAID IN REAL TIME
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            break
        except speech_recognition.UnknownValueError:
            print("Sorry, I didn't understand that.")

        
        # STOP AND SAVE 
        if (input() == ""):
            print("Saving...")
            file_name = "recordings/recording.wav"

            with open(file_name, "wb") as f:
                f.write(audio.get_wav_data())

            print("Saved!")
            break
