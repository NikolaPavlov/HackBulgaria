from mutagen.mp3 import MP3

audio = MP3("/home/rastamandito/Music/indila.mp3")
print(audio.info.length)
