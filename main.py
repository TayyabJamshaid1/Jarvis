import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
     print("Processing command: " + c)
     pass

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
          recognizer = sr.Recognizer()
          print("Recognizing...")
          try:
               with sr.Microphone() as source:
                              # print("Adjusting for ambient noise...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)  # ← ADD THIS!
                    print("Say something...")
                    audio = recognizer.listen(source,timeout=5, phrase_time_limit=5)
               
                    word = recognizer.recognize_google(audio)
                    print("You said: " + word)
                    if (word.lower()=="hello"):
                        speak("Yes Sir, How can I help you?")
                        with sr.Microphone() as source:
                             print("Jarvis Active ")
                             audio = recognizer.listen(source,timeout=5, phrase_time_limit=5)
                             command = recognizer.recognize_google(audio)
                             print("You said: " + command)
                             process_command(command)
          except sr.UnknownValueError:
               print("Google could not understand audio")
          except sr.RequestError as e:
               print("Google Speech Recognition error; {0}".format(e))