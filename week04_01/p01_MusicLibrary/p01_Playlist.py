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

    def next_song(self):
        first_song = self.songs[0]
        # using random.choice ---> random elem from list withowth replacement

        '''
        alg for random nums withowth repeat

        arr =[1,2,3,4,5]
        copy_arr =[1,2,3,4,5]


        for i in range(len(copy_arr)):
            random_elem = random.choice(copy_arr)
            print(random_elem)
            copy_arr.remove(int(random_elem))
        '''

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