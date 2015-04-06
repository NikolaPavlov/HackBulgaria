'''
from mutagen.mp3 import MP3

audio = MP3("/home/rastamandito/Music/indila.mp3")
print(audio.info.length)
'''

import re
import datetime


t = "10:15:30"
h,m,s = re.split(':', t)
print(h)

