import music21 as mus
import glob
import matplotlib.pyplot as plt

class ChordDistribution:

    def __init__(self):
        chord_distribution = None

    def get_chord_distribution(self, path):
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
            chords = score.chordify()
            print(file)
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

test = ChordDistribution()
test.get_chord_distribution('test/')
print(test.chord_distribution)
test.chord_hist()
print(test)
