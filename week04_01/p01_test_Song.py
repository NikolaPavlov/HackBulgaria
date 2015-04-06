import unittest

from p01_Song import Song


class TestAudio(unittest.TestCase):

    def setUp(self):
        self.songObj = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

    def test_constructor(self):
        self.assertTrue(isinstance(self.songObj, Song))

    #check this shit mf
    def test_to_str(self):
        self.assertTrue(str(self.songObj), "Manowar - Odin from The Sons of Odin - 3:44")

    def test_eq(self):
        self.assertTrue(self.songObj == self.songObj)

    def test_hash(self):
        self.assertIsNotNone(hash(self.songObj))

    def test_length_of_mp3_seconds(self):
        self.assertEqual(self.songObj.length_of_mp3(seconds=True), 224)

    def test_length_of_mp3_minutes(self):
        self.assertEqual(self.songObj.length_of_mp3(minutes=True), 3.73)

    def test_length_of_mp3_hours(self):
        self.assertEqual(self.songObj.length_of_mp3(hours=True), 0.06)

    def test_length_to_str(self):
        self.assertEqual(self.songObj.length_to_str(), self.songObj.length)


if __name__ == "__main__":
    unittest.main()
