import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening....")
        playsound("bot_initial.mp3")  
        try:
            
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Please speak now...")
            
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "Listening timed out. Please try again."
        except sr.UnknownValueError:
            return "Sorry, could not understand the input."
        except Exception as e:
            return f"An error occurred: {e}"

def save_input_to_file(text, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Input saved at {file_path}")
    except Exception as e:
        print(f"Failed to save input: {e}")

def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        # recognizer.recognize_google(audio, language="hi-IN")  # For Hindi
        # tts = gTTS(text=text, lang='hi')

        response_file = "response.mp3"
        tts.save(response_file)
        playsound(response_file)
    except Exception as e:
        print(f"Failed to generate or play speech: {e}")

text = listen()
print(f"Recognized text: {text}")
speak(f"You said: {text}")

file_path = 'user_input.txt'
save_input_to_file(text, file_path)
