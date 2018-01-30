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
## AGAIN - this is a terrible hack, but renaming it seems to fix a lot of stuff, but quotes etc
# are a problem at the moment.   This is a quick workaround to see if I have a mixer
# issue or a file issue
maeve_file = "./mp3/" + maeve_text + ".mp3"
#print(maeve_file)

# Check to see if the mp3 directory exists; if not - create it.
if not os.path.exists('./mp3'):
	os.makedirs('./mp3')

with open(maeve_file, 'wb') as f:
	f.write(spoken_text['AudioStream'].read())
	f.close

mixer.init()
mixer.music.load(meave_file)
mixer.music.play()

while mixer.music.get_busy() == True:
	pass

#os.remove('maeve_file')
mixer.quit()
