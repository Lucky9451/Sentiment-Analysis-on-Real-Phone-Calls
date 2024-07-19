import speech_recognition as sr


def process_audio(file_path):
    r = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio)
            with open("transcribed_text.txt", "w") as file:
                file.write(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

