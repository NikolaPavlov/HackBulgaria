import unittest

from p01_Playlist import Playlist
from p01_Song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.theList = Playlist()
        self.song1 = Song(title="bikut mucho", artist="Cherno Feredje", length="0:33")
        self.song2 = Song(title="Kaluger me goni", artist="Cherno Feredje", length="1:00")
        self.song3 = Song(title="Haskovo", artist="Cherno Feredje", length="1:00")
        self.song4 = Song(title="Ginger", artist="Cookie Monsta", length="2:00")
        self.song5 = Song(title="yyy", artist="Cookie Monsta", length="1:00")
        self.song6 = Song(title="Are you there", artist="Josh Wink", length="22:10")
        self.song7 = Song(title="Sad but true", artist="Metallica", length="40:00")
        self.songsArr = [self.song3, self.song4]
        self.theList.add_song(self.song1)

    def test_constructor(self):
        self.assertTrue(isinstance(self.theList, Playlist))

    def test_add_song(self):
        self.assertTrue(self.song1 in self.theList.songs)

    def test_remove_song(self):
        self.theList.add_song(self.song2)
        self.assertTrue(self.song1 in self.theList.songs)
        self.theList.remove_song(self.song2)
        self.assertFalse(self.song2 in self.theList.songs)

    def test_add_arr_of_songs(self):
        self.theList.add_songs(self.songsArr)
        self.assertTrue(self.song3 in self.theList.songs)
        self.assertTrue(self.song4 in self.theList.songs)

    def test_total_length_sec(self):
        self.theList = Playlist()
        self.theList.add_song(self.song1)
        self.assertEqual(self.theList.total_length(), "0:33")

    def test_total_length_min(self):
        self.theList = Playlist()
        self.theList.add_song(self.song3)
        self.theList.add_song(self.song6)
        self.assertEqual(self.theList.total_length(), "23:10")

    def test_total_length_hours(self):
        self.theList = Playlist()
        self.theList.add_song(self.song5)
        self.theList.add_song(self.song6)
        self.theList.add_song(self.song7)
        self.assertEqual(self.theList.total_length(), "1:03:10")



if __name__ == "__main__":
    unittest.main()
