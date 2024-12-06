import unittest
from soundscapes.feature_logic import Soundscape

class TestSoundscape(unittest.TestCase):
    def test_add_sound(self):
        soundscape = Soundscape("area1")
        soundscape.add_sound("bird_chirp")
        self.assertIn("bird_chirp", soundscape.sounds)

    def test_list_sounds(self):
        soundscape = Soundscape("area1", ["bird_chirp"])
        self.assertEqual(soundscape.list_sounds(), ["bird_chirp"])

if __name__ == "__main__":
    unittest.main()
