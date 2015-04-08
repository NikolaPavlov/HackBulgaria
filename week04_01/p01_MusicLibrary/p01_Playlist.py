import datetime
import random

from tabulate import tabulate
from p01_Song import Song


class Playlist:

    def __init__(self, name="", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle

        self.songs = []
        self.song_num = 0

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
            if song.artist in histogram:
                histogram[song.artist] += 1
            else:
                histogram[song.artist] = 1
        return histogram

    def next_song(self):
        # play the list once then game over
        if self.repeat is False and self.shuffle is False:
            self.current_song = self.songs[self.song_num]
            self.song_num += 1
            if self.song_num == len(self.songs):
                raise ValueError
            else:
                return self.songs[self.song_num]

        # play the list from the beggining when it's over
        if self.repeat is True and self.shuffle is False:
            self.current_song = self.songs[self.song_num]
            self.song_num += 1
            if self.song_num == len(self.songs):
                self.song_num = 0
                return self.songs[self.song_num]
            else:
                return self.songs[self.song_num]

        # play the list once on random withowth repeating single track
        if self.repeat is False and self.shuffle is True:
            if len(self.songs) == 0:
                raise ValueError("over")
            while len(self.songs) > 0:
                song_for_return = random.choice(self.songs)
                self.songs.remove(song_for_return)

                if song_for_return is None:
                    print("Fuck!")
                return song_for_return

        # full random
        if self.repeat is True and self.shuffle is True:
            pass

    def printing_the_list(self):
        output_table = []
        headers = ["Song", "Artist", "Album", "Length"]
        for song in self.songs:
            output_table.append([song.title, song.artist, song.album, song.length])

        print(tabulate(output_table, headers, tablefmt="grid"))


class ExcpPlayListOver(Exception):
    pass


def main():
    # Tests
    play_list = Playlist(repeat=False, shuffle=True)
    song1 = Song(artist="cherno feredje", length="0:33")
    song2 = Song(artist="proto", length="1:00")
    song3 = Song(artist="dnb", length="2:00")
    song4 = Song(artist="dnb", length="2:00")
    song5 = Song(artist="proto", length="1:00")
    song6 = Song(artist="proto", length="22:00")
    play_list.add_song(song1)
    play_list.add_song(song2)
    play_list.add_song(song3)
    play_list.add_song(song4)
    play_list.add_song(song5)
    play_list.add_song(song6)

    # print(play_list.total_length())
    # print(play_list.artists())
    # print(play_list.next_song())
    # print(play_list.next_song())
    # print(play_list.next_song())
    play_list.printing_the_list()

if __name__ == "__main__":
    main()
