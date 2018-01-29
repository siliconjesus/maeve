import boto3
from pygame import mixer
import os

# Assumes you already registered your API key with AWS python plugin

polly = boto3.client('polly')
maeve_voice = 'Joanna'
spoken_text = polly.synthesize_speech(Text='The Weather today is mostly sunny with a high of 48 deg$rees', OutputFormat='mp3', VoiceId=maeve_voice)

with open('output.mp3', 'wb') as f:
	f.write(spoken_text['AudioStream'].read())
	f.close

mixer.init()
mixer.music.load('output.mp3')
mixer.music.play()

while mixer.music.get_busy() == True:
	pass

mixer.quit()
