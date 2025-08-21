import speech_recognition as sr
from gtts import gTTS
import pygame
import webbrowser
import os
import time
import tempfile
import music

# Initialize pygame mixer once
pygame.mixer.init()

# Speak function using gTTS + pygame


def speak(text):
    print("Jarvis:", text)
    # Create a temporary mp3 file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:

        filename = f.name
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(filename)

    # Play the sound
    sound = pygame.mixer.Sound(filename)
    channel = sound.play()
    while channel.get_busy():
        time.sleep(0.1)

    # Stop and delete the temporary file
    sound.stop()
    os.remove(filename)

# Process commands


def Processcommand(command):
    command = command.lower()
    if "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://google.com")
    elif command.lower().startswith("play"):
        song_name = command[5:].strip()  # take everything after "play "
    if song_name in music.music:
        link = music.music[song_name]
        speak(f"Playing {song_name}")
        webbrowser.open(link)
    else:
        speak(f"Sorry, I don't have {song_name} in the library")


# Main loop
if __name__ == "__main__":
    recognizer = sr.Recognizer()
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(
                    source, timeout=5, phrase_time_limit=4)

            wake_word = recognizer.recognize_google(audio).lower()
            print("You said:", wake_word)

            if "jarvis" in wake_word:
                speak("Yes?")
                time.sleep(0.2)

                with sr.Microphone() as source:
                    print("Listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(
                        source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                print("Command:", command)
                Processcommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except Exception as e:
            print("Error:", e)
