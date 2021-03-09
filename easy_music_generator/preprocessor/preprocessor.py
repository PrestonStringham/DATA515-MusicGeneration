from preprocessor.note_distribution import NoteDistribution
from preprocessor.chord_distribution import ChordDistribution
import music21 as mus
import glob

class Preprocessor:

    def __init__(self):
        self.scores = None

    def parse_scores(self, path):
        #Look for MusicXML and MIDI Files
        mxlfiles = [f for f in glob.glob(path + "*.mxl")]
        midifiles = [f for f in glob.glob(path + "*.mid")]
        files = mxlfiles + midifiles
        #If no MIDI or MusicXML files exist, raise exception
        score_objects = []

        if len(files) == 0:
            raise NoFilesFoundException()

        for file in files:
            score = mus.converter.parse(file)
            score_objects.append(score)
        self.scores = score_objects

        return self.scores

    def get_note_matrix(self):
        return NoteDistribution.get_note_matrix(self.scores)

    def get_chord_matrix(self):
        return ChordDistribution.get_chord_matrix(self.scores)


class NoFilesFoundException(Exception):
    def __init__(self, message="No MIDI or MusicXML files found in the provided directory. Please check the path."):
        self.message = message
        super().__init__(self.message)
