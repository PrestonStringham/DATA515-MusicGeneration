from easy_music_generator.preprocessor.note_distribution import (
        NoteDistribution)

from easy_music_generator.preprocessor.chord_distribution import (
        ChordDistribution)

import music21 as mus
import glob


class Preprocessor:
    '''
    This class contains methods to process MIDI and/or MXL files
    provided by user.  The objective is to understand the distribution
    of notes and chords in the songs.  After processing it, the output
    are a note probability matrix and a chord probability matrix.
    '''
    def __init__(self):
        self.scores = None

    def parse_scores(self, path):
        '''
        This method takes MIDI and MusicXML files as input and it
        outputs a list of score objects.

        Scores are a Music21 objects that allows to represent multi-part
        music in a usable data format.
        '''
        # Look for MusicXML and MIDI Files
        mxlfiles = [f for f in glob.glob(path + "*.mxl")]
        midifiles = [f for f in glob.glob(path + "*.mid")]
        files = mxlfiles + midifiles

        # If no MIDI or MusicXML files exist, raise exception
        if len(files) == 0:
            raise NoFilesFoundException()

        score_objects = []
        for file in files:
            score = mus.converter.parse(file)
            score_objects.append(score)
        self.scores = score_objects

        return self.scores

    def get_note_matrix(self):
        '''
        This method returns a matrix with the probability of occurrence
        of notes in a melody.
        '''
        return NoteDistribution.get_note_matrix(self.scores)

    def get_chord_matrix(self):
        '''
        This method returns a matrix with the probability of occurrence
        of chords in a song.
        '''
        return ChordDistribution.get_chord_matrix(self.scores)


class NoFilesFoundException(Exception):
    def __init__(self,
                 message="No MIDI or MusicXML files found in the \
                 provided directory. Please check the path."):
        self.message = message
        super().__init__(self.message)
