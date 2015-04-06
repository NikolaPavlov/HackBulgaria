from mutagen.mp3 import MP3
from datetime import datetime, timedelta


class Song:

    def __init__(self, title="", artist="", album="", length=0):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        '''
        titles = self.title == other.title
        artists = self.artist == other.artist
        albums = self.album == other.album
        lengths = self.length == other.length
        return titles and artists and albums and lengths
        '''

        if self.title == other.title:
            if self.artist == other.artist:
                if self.album == other.album:
                    if self.length == other.length:
                        return True
                    return False
                return False
            return False
        return False

    def __hash__(self):
        return hash(self.title)

    def length_of_mp3(self, seconds=False, minutes=False, hours=False):
        parts = self.length.split(":")
        seconds = int(parts[0])*(60*60) + int(parts[1])*60 + int(parts[2])
        if seconds:
            return seconds
        elif minutes:
            return seconds / 60
        elif hours:
            return seconds / 60 * 60
        else:
            raise ValueError

    def length_to_str(self):
        return self.length


#Tests
song1 = Song(title="ma faka", length="1:22:22", artist="gogo band", album="no album")
print(str(song1))