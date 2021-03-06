import music21 as mus
import glob
import matplotlib.pyplot as plt

class ChordDistribution:

    def __init__(self):
        pass

    @staticmethod
    def get_chord_matrix(scores):
        dic = {}
        for score in scores:
            chords = score.chordify()
            for i in range(len(chords.recurse().getElementsByClass('Chord'))-1):
            #Iterate through list of notes/counts and add the count of each note to the dictionary
            #for n in sorted(nameOctaveCount):
                chord_notes = chords[i].notes
                print(chord_notes)

class NoFilesFoundException(Exception):
    def __init__(self, message="No MIDI or MusicXML files found in the provided directory. Please check the path."):
        self.message = message
        super().__init__(self.message)

class NoNotesFoundException(Exception):
    def __init__(self, message="The provided MIDI or MusicXML files do not contain any notes."):
        self.message = message
        super().__init__(self.message)
