import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening....")
        playsound("bot_initial.mp3")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "Listening timed out. Please try again."
        except sr.UnknownValueError:
            return "Sorry, could not understand the input."

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound("response.mp3")

text = listen()
print(f"Recognized text: {text}")
speak(f"You said: {text}")
