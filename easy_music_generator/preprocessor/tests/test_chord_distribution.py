import unittest
from easy_music_generator.preprocessor import chord_distribution as cd
import music21 as mus


class TestChordDistribution(unittest.TestCase):
    """
    Unit tests for chord_distribution.py, a preprocessor module
    """
    def test_get_chord_matrix(self):
        '''
        Test get_chord_matrix(), the function takes a music21 Score object
        and returns the prbability dictionary
        '''

        # Create a Score object with two chords to process and get probability
        s = mus.stream.Score()
        c1 = mus.chord.Chord(['D', 'F#', 'A'])
        c2 = mus.chord.Chord('A4 C#5 E5')

        s.append(c1)
        s.append(c2)

        expected_output = {'[62, 66, 69]': 0.5, '[69, 73, 76]': 0.5}
        actual_output = cd.ChordDistribution.get_chord_matrix([s])
        self.assertEqual(expected_output, actual_output)

    def test_get_chord_matrix_chordify(self):
        '''
        Unit tests get_chord_matrix() when the score object doesn't
        have chords. Mainly to test chordify files
        '''
        # Score object that doesn't contain any chords
        no_chord_score_obj = mus.stream.Score()
        no_chord_score_obj.append(mus.note.Note('G9'))
        no_chord_score_obj.append(mus.note.Note('F9'))
        expected_output = {'[127]': 0.5, '[125]': 0.5}

        chord_distro = cd.ChordDistribution()
        actual_output = chord_distro.get_chord_matrix([no_chord_score_obj])
        self.assertEqual(expected_output, actual_output)

    def test_get_chord_matrix_raise_no_note_exception(self):
        '''
        Test that get_chord_matrix() raises an exception when the score
        object it gets does not contain any chords
        '''

        # Create an empty Score object to raise the exception
        s1 = mus.stream.Score()
        with self.assertRaises(cd.NoChordsFoundException) as context:
            cd.ChordDistribution.get_chord_matrix([s1])

        self.assertEqual(
            context.exception.message,
            "The provided MIDI or MusicXML files do not contain any chords.")

    def test_get_chord_probabilities(self):
        '''
        Test get_chord_probabilities(), the function takes a dictionary
        of chord counts and returns a dictionary of the chord probabilities
        '''

        my_chord_dict = {'chord_1': 1, 'chord_2': 1}
        # Test the method as a static method
        _ = cd.ChordDistribution.get_chord_probabilities(my_chord_dict)
        self.assertEqual(my_chord_dict['chord_1'], 0.5)
        self.assertEqual(my_chord_dict['chord_2'], 0.5)

        # Test the method as an instance method
        chord_distro = cd.ChordDistribution()
        _ = chord_distro.get_chord_probabilities(my_chord_dict)
        self.assertEqual(my_chord_dict['chord_1'], 0.5)
        self.assertEqual(my_chord_dict['chord_2'], 0.5)
