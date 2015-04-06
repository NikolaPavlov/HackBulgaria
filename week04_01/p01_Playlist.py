from p01_Song import Song


#code_songs = Playlist(name="Code", repeat=True, shuffle=True)

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
        self.songs.append(songsArr)

song1 = Song(title="ma faka", length="1:22:22", artist="gogo band", album="no album")
theList = Playlist()
theList.add_song(song1)
print(theList.songs)