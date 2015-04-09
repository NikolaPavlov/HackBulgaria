'''
from mutagen.mp3 import MP3

audio = MP3("/home/rastamandito/Music/indila.mp3")
print(audio.info.length)
'''

import random

arr =[1,2,3,4,5]
copy_arr =[1,2,3,4,5]

'''
for i in range(len(copy_arr)):
    random_elem = random.choice(copy_arr)
    print(random_elem)
    copy_arr.remove(int(random_elem))
'''

'''
x = [arr[i] for i in range(len(arr))]
random.shuffle(x)
print(x)
'''
print(random.shuffle)