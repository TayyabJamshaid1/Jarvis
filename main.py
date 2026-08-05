import speech_recognition as sr
import webbrowser
import pyttsx3
import naatLibrary
# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
     print("Processing command: " + c)
     if "open google" in c.lower():
          speak("Opening Google")
          webbrowser.open("https://www.google.com")
     elif "open youtube" in c.lower():
          speak("Opening YouTube")
          webbrowser.open("https://www.youtube.com")
     elif "open facebook" in c.lower():
          speak("Opening Facebook")
          webbrowser.open("https://www.facebook.com")
     elif "open instagram" in c.lower():
          speak("Opening Instagram")
          webbrowser.open("https://www.instagram.com")
     elif c.lower().startswith("play"):
          print("Playing naat")
          naat_name=c.split(" ")[1]
          print("Naat name: " + naat_name.lower())
          link=naatLibrary.naat[naat_name.lower()]
          speak(f"Playing {naat_name}")
          webbrowser.open(link)


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
                        speak("Yeah")
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