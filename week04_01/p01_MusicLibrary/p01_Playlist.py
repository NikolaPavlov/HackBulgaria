import time
import datetime
import random
import json
import os
import mutagen

from tabulate import tabulate
from p01_Song import Song


class Playlist:

    def __init__(self, name="", repeat=False, shuffle=False):
        self.name = name.replace(' ', '-')
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

        # We have hours, add them to output
        if total_length / (60 * 60) > 1:
            return str(datetime.timedelta(seconds=total_length))
        # Output only minutes and seconds
        elif total_length / 60 > 0:
            return_minutes = total_length // 60
            return_seconds = total_length % 60
            return "{}:{}".format(return_minutes, return_seconds)
        else:
            raise ValueError

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

        # play with random and repeat when it's over
        # need fixes (repeating songs, before end of playlist)
        if self.repeat is True and self.shuffle is True:
            # shuffle the songs
            shuffled_songs = [self.songs[i] for i in range(len(self.songs))]
            random.shuffle(shuffled_songs)
            self.songs = shuffled_songs

            self.current_song = self.songs[self.song_num]
            self.song_num += 1
            if self.song_num == len(self.songs):
                self.song_num = 0
                return self.songs[self.song_num]
            else:
                return self.songs[self.song_num]

    def printing_the_list(self):
        output_table = []
        headers = ["Artist", "Song", "Album", "Length"]
        for song in self.songs:
            output_table.append([song.artist, song.title, song.album, song.length])

        print(tabulate(output_table, headers, tablefmt="grid"))

    def prepare_json(self):
        data = {
        "name": self.name,
        "songs": [song.__dict__ for song in self.songs]
        }

        return data

    def save(self, indent=True):
        filename = self.name.replace(" ", "-") + ".json"

        with open(filename, 'w') as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            content = json.load(f)
            the_play_list = Playlist(content["name"])
            for song in content["songs"]:
                loaded_song = Song(artist=song["artist"], title=song["title"], album=song["album"], length=song["length"])
                the_play_list.add_song(loaded_song)
            return the_play_list


def test_save():
    play_list = Playlist(name="the play list", repeat=True, shuffle=True)
    song1 = Song(title="BikutMucho", artist="ChernoFeredje", length="0:33")
    song2 = Song(title="KalugerMeGoni", artist="ChernoFeredje", length="1:00")
    song3 = Song(title="Haskovo", artist="ChernoFeredje", length="2:00")
    song4 = Song(title="Ginger", artist="CookieMonsta", length="2:00")
    song5 = Song(title="yyy", artist="CookieMonsta", length="1:00")
    song6 = Song(title="AreYouThere", artist="JoshWink", length="22:00")
    play_list.add_song(song1)
    play_list.add_song(song2)
    play_list.add_song(song3)
    play_list.add_song(song4)
    play_list.add_song(song5)
    play_list.add_song(song6)
    play_list.printing_the_list()
    play_list.save()


def test_load():
        p = Playlist.load("the-play-list.json")
        try:
            while True:
                song = p.next_song()
                print(str(song))
                time.sleep(1)
        except Exception as e:
            print(e)


class ExcpPlayListOver(Exception):
    pass


# ############################################################################


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def get_info(self, data):
        song_data = {}
        try:
            song_data["artist"] = data["TPE1"].text[0]
        except:
            song_data["artist"] = "Unknown Artist"
        try:
            song_data["album"] = data["TALB"].text[0]
        except:
            song_data["album"] = "Unknown Album"
        try:
            song_data["title"] = data["TIT2"].text[0]
        except:
            song_data["title"] = "Unknown Title"
        try:
            song_data["length"] = str(
    datetime.timedelta(seconds=data.info.length // 1))[2:]
        except:
            song_data["length"] = "Unknown"

        return song_data

    def generate_playlist(self, name):
        playlist = Playlist(name)
        songs = [mp3 for mp3 in os.listdir(self.path) if mp3.endswith(".mp3")]
        for song in songs:
            data = mutagen.File(self.path + "/" + song)
            info = self.get_info(data)
            new_song = Song(
                artist=info["artist"], title=info["title"], album=info["album"], length=info["length"])
            playlist.add_song(new_song)
        return playlist


# ############################################################################


if __name__ == "__main__":
    # test_save()
    test_load()
    # my_crawler = MusicCrawler("/home/username/Music/AlbumFolder")
    # listt = my_crawler.generate_playlist('gogo')
    # listt.printing_the_list()
