import os
import glob
import unittest
from easy_music_generator import easy_music_generator as emg


class TestEasyMusicGenerator(unittest.TestCase):
    """
    Unit tests for easy_music_generator.py
    """

    def setUp(self):

        pre_exist = glob.glob('./output/*.mid')

        if len(pre_exist):
            for midi in pre_exist:
                os.remove(midi)

        if os.path.exists("./output"):
            os.rmdir("./output")

    def test_easy_music_generator(self):
        emg_obj = emg.EasyMusicGenerator()

        input_file_path = './easy_music_generator/music/'
        emg_obj.analyze(input_file_path)

        output_file_path = 'output/'
        number_of_bars = 10
        emg_obj.generate(number_of_bars, output_file_path)

        out_midi = glob.glob('./output/*.mid')
        self.assertNotEqual(len(out_midi), 0)
