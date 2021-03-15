import unittest
import preprocessor.preprocessor as p


class TestPreprocessor(unittest.TestCase):
    def test_parse_scores(self):

        '''
            Test that parse_scores() returns a score in the form of a list.
            Not testing for actual score accuracy as it changes every run.
        '''

        preprocessor_obj = p.Preprocessor()
        score = preprocessor_obj.parse_scores("./music/test_parse_scores/")

        self.assertEqual("<class 'list'>", str(type(score)))

    def test_parse_scores_no_files_found_exception(self):

        '''
        Test that parse_scores() raises an exception when the filepath
        parameter does not contain any files.
        '''

        filepath = "./music/test_no_files_exception/"
        preprocessor_obj = p.Preprocessor()
        with self.assertRaises(p.NoFilesFoundException) as context:
            preprocessor_obj.parse_scores(filepath)

        self.assertEqual(
            context.exception.message,
            "No MIDI or MusicXML files found in "
                 "the provided directory. Please check the path.")



