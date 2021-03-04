import NoteDistribution as nd
import ChordDistribution as cd
import music21 as mus

import glob
class Preprocessor:

    def __init__(self):
        self.scores = None
        self.note_matrix = None
        self.chord_matrix = None
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
        note_dist = nd.NoteDistribution()
        self.note_matrix = note_dist.get_note_matrix(self.scores)
        return self.note_matrix

    def get_chord_matrix(self):
        chord_dist = cd.ChordDistribution()
        self.chord_matrix = chord_dist.get_chord_matrix(self.scores)
        return self.chord_matrix
