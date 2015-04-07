import datetime
from p01_Song import Song


class Playlist:

    def __init__(self, name="", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle

        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def add_songs(self, songsArr):
        for song in songsArr:
            self.add_song(song)

    def total_length(self):
        total_length = 0
        for song in self.songs:
            total_length += song.length_of_mp3(seconds=True)
        # Format the return format
        return str(datetime.timedelta(seconds=total_length))

    def artists(self):
        # histogram of artists
        histogram = {}
        for song in self.songs:
            histogram[repr(song)] = self.songs.count(song)
        return histogram


# Tests
play_list = Playlist()
song1 = Song(artist="cherno feredje", length="0:33")
song2 = Song(artist="proto", length="1:00")
song3 = Song(artist="dnb", length="2:00")
song4 = Song(artist="dnb", length="2:00")
song5 = Song(artist="proto", length="1:00")
play_list.add_song(song1)
play_list.add_song(song2)
play_list.add_song(song3)
play_list.add_song(song5)
play_list.add_song(song4)

#print(play_list.total_length())
print(play_list.artists())