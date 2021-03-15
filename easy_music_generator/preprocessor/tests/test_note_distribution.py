import unittest
import preprocessor.note_distribution as nd
import numpy as np
import music21 as mus


class TestNoteDistribution(unittest.TestCase):
    """
    Unit tests for note_distribution.py, a preprocessor module
    """

    def test_get_note_matrix(self):

        '''
        Test get_note_matrix(), the function takes a music21 Score object
        and returns the stochastic matrix and a probability dictionary
        '''

        # dummy Score object with two notes
        dummy_score_obj = mus.stream.Score()
        dummy_score_obj.append(mus.note.Note('G9'))
        dummy_score_obj.append(mus.note.Note('F9'))

        # the expected stochastic matrix of the two notes
        expected_matrix = np.zeros((128, 128), dtype=float)
        expected_matrix[127, 125] = 1

        # the expected probability dictionary of the two notes
        expected_prob_dic = {'125': 0.5, '127': 0.5}
        expected_tuple = (expected_matrix, expected_prob_dic)
        actual_tuple = nd.NoteDistribution.get_note_matrix([dummy_score_obj])

        # use np.allclose to check whether the two
        # matrices are equal within a tolerance
        self.assertTrue(np.allclose(expected_tuple[0],
                        actual_tuple[0], rtol=1e-05, atol=1e-08))

        # check if the two probability dictionary are equal
        self.assertEqual(expected_tuple[1], actual_tuple[1])

    def test_get_note_matrix_raise_no_note_exception(self):
        '''
        Test that get_note_matrix() raises an exception when the score
        object it gets does not contain any notes
        '''
        score = mus.converter.parse('./music/test_no_notes_exception.xml')
        with self.assertRaises(nd.NoNotesFoundException) as context:
            nd.NoteDistribution.get_note_matrix([score])

        self.assertEqual(
            context.exception.message,
            "The provided MIDI or MusicXML "
            "files do not contain any notes.")

    def test_get_stochastic_note_matrix(self):
        '''
        Test get_stochastic_note_matrix(), the function takes a
        dictionary of note positions and returns a 128x128 matrix of MIDI notes
        '''
        input_distribution = {'0 1': 1, '127 127': 1}
        expected_output = np.zeros((128, 128), dtype=float)
        expected_output[0, 1] = 1
        expected_output[127, 127] = 1
        actual_output_true = nd.NoteDistribution.get_stochastic_note_matrix(
                                                input_distribution)
        self.assertTrue(np.allclose(actual_output_true,
                                    expected_output, rtol=1e-05, atol=1e-08))
        expected_output[127, 124] = 1
        actual_output_false = nd.NoteDistribution.get_stochastic_note_matrix(
                                                input_distribution)
        self.assertFalse(np.allclose(actual_output_false,
                                     expected_output, rtol=1e-05, atol=1e-08))

    def test_get_note_probabilities(self):
        '''
        Test get_note_probabilities(), the function takes a dictionary
        of notes count and returns a dictionary of the note probabilities
        '''
        input_distribution = {'60': 2, '55': 1, '83': 1}
        expected_output = {'60': 0.5, '55': 0.25, '83': 0.25}

        # Test the method as a static method
        self.assertEqual(nd.NoteDistribution.get_note_probabilities(
                                    input_distribution), expected_output)

        # Test the method as an instance method
        note_distribution = nd.NoteDistribution()
        self.assertEqual(note_distribution.get_note_probabilities(
                                    input_distribution), expected_output)
