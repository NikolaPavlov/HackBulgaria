import unittest

from mutagen.mp3 import MP3
from p01_Song import Song


class TestAudio(unittest.TestCase):

    def setUp(self):
        self.songObj = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="00:03:44")

    def test_constructor(self):
        self.assertTrue(isinstance(self.songObj, Song))

    #check this shit mf
    def test_to_str(self):
        self.assertTrue(str(self.songObj), "Manowar - Odin from The Sons of Odin - 3:44")

    def test_eq(self):
        self.assertTrue(self.songObj == self.songObj)

    def test_hash(self):
        self.assertIsNotNone(hash(self.songObj))

    def test_length_of_mp3(self):
        self.assertTrue(self.songObj.length_of_mp3(seconds=True), 224)

'''
    def test_length_error(self):
        with self.assertRaises(ValueError):
            self.songObj.length_of_mp3(seconds="testSeconds")
'''
    






if __name__ == "__main__":
    unittest.main()
