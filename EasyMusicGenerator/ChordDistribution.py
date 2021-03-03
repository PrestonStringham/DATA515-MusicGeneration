import music21 as mus
import glob
import matplotlib.pyplot as plt

class ChordDistribution:

    def __init__(self):
        chord_distribution = None

    def get_chord_matrix(self, scores):
        dic = {}
        for score in scores:
            chords = score.chordify()
            for chord in chords.recurse().getElementsByClass('Chord'):
            #Iterate through list of notes/counts and add the count of each note to the dictionary
            #for n in sorted(nameOctaveCount):
                forteclass = chord.pitchedCommonName
                if forteclass in dic:
                    dic[forteclass] += 1
                else:
                    dic[forteclass] = 1
        self.chord_distribution = dic
        return self.chord_distribution

    def chord_hist(self):
        ind = [i for i in range(len(self.chord_distribution))]
        fig, ax = plt.subplots()
        ax.bar(ind, self.chord_distribution.values())
        plt.xticks(ind, self.chord_distribution.keys(), rotation='vertical')
        plt.show()

class NoFilesFoundException(Exception):
    def __init__(self, message="No MIDI or MusicXML files found in the provided directory. Please check the path."):
        self.message = message
        super().__init__(self.message)

class NoNotesFoundException(Exception):
    def __init__(self, message="The provided MIDI or MusicXML files do not contain any notes."):
        self.message = message
        super().__init__(self.message)