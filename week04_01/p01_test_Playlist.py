import unittest

from p01_Playlist import Playlist
from p01_Song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.theList = Playlist()
        self.song1 = Song()
        self.song2 = Song(artist="Prodigy")
        self.theList.add_song(self.song1)
        print(self.theList.songs)

    def test_constructor(self):
        self.assertTrue(isinstance(self.theList, Playlist))

    def test_add_song(self):
        self.assertTrue(str(self.song1) in self.theList.songs)

    def test_remove_song(self):
        self.assertFalse(str(self.song2) in self.theList.songs)

if __name__ == "__main__":
    unittest.main()