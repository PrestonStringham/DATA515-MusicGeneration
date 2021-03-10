import unittest
import preprocessor.chord_distribution as cd

class TestChordDistribution( unittest.TestCase ):

    def test_get_chord_probabilities( self ):
        #
        # Print a blank separator line.
        #
        print()

        chord_distro = cd.ChordDistribution()

        my_chord_dict = { 'chord_1': 1, 'chord_2': 1 }

        print( cd.ChordDistribution.get_chord_probabilities( my_chord_dict ) )
        print( chord_distro.get_chord_probabilities( my_chord_dict ) )


# --- END --- #

