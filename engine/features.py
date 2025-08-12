from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os

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