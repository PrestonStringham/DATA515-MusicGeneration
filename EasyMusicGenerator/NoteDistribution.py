import music21 as mus
import matplotlib.pyplot as plt

class NoteDistribution:

    def __init__(self):
        note_distribution = None

    def get_note_matrix(self, scores):
        dic = {}
        for score in scores:
            nameOctaveCount = mus.analysis.pitchAnalysis.pitchAttributeCount(score, 'nameWithOctave')
            #Iterate through list of notes/counts and add the count of each note to the dictionary
            for n in sorted(nameOctaveCount):
                if n in dic.values():
                    dic[n] += nameOctaveCount[n]
                else:
                    dic[n] = nameOctaveCount[n]
            if len(dic.keys()) == 0:
                raise NoNotesFoundException()
            self.note_distribution = dic
            return self.note_distribution

    def note_hist(self):
        ind = [i for i in range(len(self.note_distribution))]
        fig, ax = plt.subplots()
        ax.bar(ind, self.note_distribution.values())
        plt.xticks(ind, self.note_distribution.keys(), rotation='vertical')
        plt.show()

class NoFilesFoundException(Exception):
    def __init__(self, message="No MIDI or MusicXML files found in the provided directory. Please check the path."):
        self.message = message
        super().__init__(self.message)

class NoNotesFoundException(Exception):
    def __init__(self, message="The provided MIDI or MusicXML files do not contain any notes."):
        self.message = message
        super().__init__(self.message)
