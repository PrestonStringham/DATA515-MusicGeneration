import os
import glob
import unittest
import easy_music_generator as emg


class TestEasyMusicGenerator(unittest.TestCase):
    """
    Unit tests for easy_music_generator.py
    """

    def setUp(self):

        import pdb
        pdb.set_trace()
        pre_exist = glob.glob( './output/*.mid' )

        if len( pre_exist ):
            for midi in pre_exist:
                os.remove( midi )

        if os.path.exists( "./output" ):
            os.rmdir( "./output" )

    def test_easy_music_generator(self):
        emg_obj = emg.EasyMusicGenerator()

        emg_obj.analyze('music/')
        emg_obj.generate(140, 10, 'output/')
        out_midi = glob.glob( './output/*.mid' )
        self.assertNotEqual( len( out_midi ), 0 )
