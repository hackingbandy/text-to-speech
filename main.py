from gtts import gTTS
import time 
import datetime

ts = time.time()
date_now = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def textToSpeach(text):
    tts = gTTS(text, lang="en")
    tts.save(date_now+"-"+text+".mp3")

with open("text.txt", encoding="utf8") as f:
    for line in f:
        #for word in line.split():
        try:
            textToSpeach(line)
            print(line)
        except Exception:
            pass