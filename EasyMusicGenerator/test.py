import music21 as mus
import glob
import matplotlib.pyplot as plt

class NoteDistribution:

    def __init__(self):
        note_distribution = None

    def get_note_distribution(self, path):
        #Look for MusicXML and MIDI Files
        mxlfiles = [f for f in glob.glob(path + "*.mxl")]
        midifiles = [f for f in glob.glob(path + "*.mid")]
        files = mxlfiles + midifiles
        #If no MIDI or MusicXML files exist, raise exception
        if len(files) == 0:
            raise NoFilesFoundException()
        dic = {}
        for file in files:
            score = mus.converter.parse(file)
            #Output of pitchAttributeCount is list of the counts of each pitch in the file.
            #Takes form 'A4', 'B-3', or 'C#5'.
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

test = NoteDistribution()
test.get_note_distribution('test/')
print(test.note_distribution)
test.note_hist()
print(test)
