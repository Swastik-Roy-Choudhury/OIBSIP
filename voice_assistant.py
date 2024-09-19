import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition engine and text-to-speech engine
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

# Function to listen to voice commands
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, there was an error with the speech recognition service.")
            return None

# Function to process commands
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        today = datetime.date.today()
        speak(f"Today's date is {today}.")
    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching for {query}.")
    else:
        speak("Sorry, I can't help with that.")

# Main function to run the voice assistant
def run_voice_assistant():
    speak("Voice assistant is now active.")
    while True:
        command = listen_command()
        if command:
            if "exit" in command:
                speak("Goodbye")
                break
            process_command(command)

# Run the voice assistant
if __name__ == "__main__":
    run_voice_assistant()