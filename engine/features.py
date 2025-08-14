from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os
import pywhatkit as kit
import re


# sound function for playing sound

def playAssistantSound():
    music_dir="www\\assets\\audio\\start-sound.mp3"
    playsound(music_dir)

# click Sound for mic Button

@eel.expose
def playClickSound():
    music_dir="www\\assets\\audio\\click_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speak("Opening "+ query)
        os.system('start ' + query)

    else:
        speak(f"{query} not found")


def PlayYoutube(query):
    search_item = extract_yt_term(query)
    if search_item:
        speak("Playing "+ search_item + " on YouTube")
        kit.playonyt(search_item)
    else:
        speak("Sorry, I couldn't find what to play on YouTube.")


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None