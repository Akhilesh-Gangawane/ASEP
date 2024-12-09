import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine=pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio=recognizer.listen(source, timeout=4, phrase_time_limit=5)
        try:
            text=recognizer.recognize_google(audio)
            return text 
        except sr.UnknownValueError:
            return "Sorry could not understand the input"
def speak(text):
    engine.say(text)
    engine.runAndWait()

text =listen()
print(f"Recognized text: {text}")
speak(f"You said {text}")