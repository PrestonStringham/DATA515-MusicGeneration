import unittest
import easy_music_generator as emg


class TestEasyMusicGenerator(unittest.TestCase):
    """
    Unit tests for easy_music_generator.py
    """

    def test_easy_music_generator(self):
        emg_obj = emg.EasyMusicGenerator()

        emg_obj.analyze('music/')
        emg_obj.generate(140, 10, 'output/')
        self.assertTrue(True)
