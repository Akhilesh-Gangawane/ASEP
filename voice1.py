import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening....")
        engine.say("Hi, this is Amrita listening...")
        engine.runAndWait()
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "Listening timed out. Please try again."
        except sr.UnknownValueError:
            return "Sorry, could not understand the input."

def speak(text):
    engine.say(text)
    engine.runAndWait()

text = listen()
print(f"Recognized text: {text}")
speak(f"You said: {text}")
