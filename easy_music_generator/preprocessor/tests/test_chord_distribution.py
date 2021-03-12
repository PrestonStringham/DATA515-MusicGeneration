import unittest
import preprocessor.chord_distribution as cd


class TestChordDistribution(unittest.TestCase):

    def test_get_chord_probabilities(self):
        #
        # Print a blank separator line.
        #
        print()

        chord_distro = cd.ChordDistribution()

        my_chord_dict = {'chord_1': 1, 'chord_2': 1}

        #
        # Test the method as a static method
        #
        _ = cd.ChordDistribution.get_chord_probabilities(my_chord_dict)
        self.assertEqual(my_chord_dict['chord_1'], 0.5)
        self.assertEqual(my_chord_dict['chord_2'], 0.5)

        #
        # Test the method as an instance method
        #
        _ = chord_distro.get_chord_probabilities(my_chord_dict)
        self.assertEqual(my_chord_dict['chord_1'], 0.5)
        self.assertEqual(my_chord_dict['chord_2'], 0.5)
