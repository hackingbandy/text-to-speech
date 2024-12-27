from gtts import gTTS
import time 
import datetime

from pathlib import Path

filepath = "text.txt"
filename = Path(filepath).stem
print(filename)

# Get current timestamp
ts = time.time()
time_stmp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

try:
    # Read the entire content of 'text.txt'
    with open(filepath, encoding="utf8") as f:
        content = f.read().strip()

    # Convert text to speech and save as MP3 with a fixed filename
    tts = gTTS(content, lang='en', tld= "com.au")
    output_filename = f"{time_stmp}_{filename}.mp3"
    tts.save("audio/"+output_filename)

    print(f"Successfully converted entire file to MP3: {output_filename}")

except Exception as e:
    print(f"An error occurred while processing the file: {str(e)}")
