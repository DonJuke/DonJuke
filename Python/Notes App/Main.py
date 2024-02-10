import speech_recognition as sr
import gtts
from playsound import playsound
import os
from datetime import datetime
from APIclient import NotionClient

token = "paste your token here"
database_id = "paste your data base here"
client = NotionClient(token, database_id)


r = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError:
        print("could not request results from API")
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        #tempfile = "./text.mp3"
        tempfile = os.path.dirname(__file__) + 'audio.mp3'

        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("could not play sound")
        
ACTIVATION_COMMAND = "hey google"

if __name__ == "__main__":

    while True:
        a = get_audio()
        command = audio_to_text(a)

        if ACTIVATION_COMMAND in command.lower():
            print("activate")
            play_sound("Yes Father")

            note = get_audio()
            note = audio_to_text(note)

            if note:
                play_sound(note)
            
                now = datetime.now().astimezone().isoformat()
                res = client.create_page(note, now, status="Active")
                if res.status_code == 200:
                        play_sound("Stored new item")
                if res.status_code != 200:
                        play_sound("This shit wrong as fuck")