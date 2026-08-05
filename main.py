import speech_recognition as sr
import webbrowser
import pyttsx3

if __name__ == "__main__":
    # Initialize the recognizer and text-to-speech engine
    recognizer = sr.Recognizer() #Recognizer class is used to recognize speech from audio input 
    engine = pyttsx3.init() #initialize the text-to-speech engine

    def speak(text):
        engine.say(text) #convert text to speech

    speak("Hello! I am your voice assistant. How can I help you today?") #greet the user

   