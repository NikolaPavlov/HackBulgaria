import unittest

from p01_Playlist import Playlist
from p01_Song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.theList = Playlist()
        self.song1 = Song()
        self.song2 = Song(artist="Prodigy", length="1:00")
        self.song3 = Song(artist="Cookie monsta", length="2:00")
        self.song4 = Song(artist="Anime", length="0:10")
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

    def test_total_length(self):
        self.theList.add_songs([self.song2, self.song3, self.song4])
        self.assertEqual(self.theList.total_length(), "0:03:10")

if __name__ == "__main__":
    unittest.main()
