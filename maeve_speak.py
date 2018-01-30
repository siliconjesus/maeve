import boto3
from pygame import mixer
import os
import sys

# Start with a simple tutorial and extend it to a general liberary eventually.

# Assumes you already registered your API key with AWS python plugin

polly = boto3.client('polly')
maeve_voice = 'Joanna'
maeve_text = sys.argv[1]
spoken_text = polly.synthesize_speech(Text=maeve_text, OutputFormat='mp3', VoiceId=maeve_voice)

with open('output.mp3', 'wb') as f:
	f.write(spoken_text['AudioStream'].read())
	f.close

mixer.init()
mixer.music.load('output.mp3')
mixer.music.play()

while mixer.music.get_busy() == True:
	pass

#os.remove('output.mp3')
mixer.quit()
