from p01_Song import Song


class Playlist:

    def __init__(self, name="", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle

        self.songs = []

    def add_song(self, song):
        self.songs.append(str(song))

    def remove_song(self, song):
        self.songs.remove(song)

    def add_songs(self, songsArr):
        for song in songsArr:
            self.add_song(str(song))

    def total_length(self):
        pass

# Tests
play_list = Playlist()
song1 = Song(artist="cherno feredje", length="10:00")
song2 = Song(artist="proto", length="1:00")
play_list.add_song(song1)
play_list.add_song(song2)
play_list.total_length()