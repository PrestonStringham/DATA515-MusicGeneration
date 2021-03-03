import music21 as mus
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
import matplotlib.pyplot as plt

class NoteDistribution:

    def __init__(self):
        note_distribution = None

    def get_note_matrix(self, scores):
        #Dictionary to store probabilites of neighboring notes
        dic = {}
        #iterate through all the scores
        for score in scores:
            #I don't think this line is needed
            part_stream = score.parts.stream()

            #The actual list of notes
            notes = score.flat.notes
            itr = iter(range(len(notes) - 1))
            #Iterate through all the notes
            for i in itr:
                #Make sure all the notes are ACTUALLY notes...
                if not isinstance(notes[i], mus.note.Note) or not isinstance(notes[i+1], mus.note.Note):
                    continue
                #Create pairs of notes that will later be parsed for stochastic matrix
                pair = str(notes[i].pitch.midi) + " "  + str(notes[i+1].pitch.midi)

                #Add them to the dictionary
                if pair in dic:
                    dic[pair] += 1
                else:
                    dic[pair] = 1
            #Check if the notes are actually being added to the dictionary 
            #We could have issues if a file ONLY has chords
            if len(dic.keys()) == 0:
                raise NoNotesFoundException()

            #Get the total number of notes
            total = sum(dic.values())

            #Normalize counts of notes by total
            for i in dic.keys():
                dic[i] /= total

            stochastic_matrix = self.get_stochastic_note_matrix(dic)
            return stochastic_matrix

    def get_stochastic_note_matrix(self, distribution):
        #128 total MIDI notes
        size = 128

        #Create matrix of 128x128, one row and column for each MIDI note
        matrix = np.zeros((size, size), dtype=float)
        for i in distribution.keys():
            value = distribution[i]
            #MIDI note values were kept as strings in the dictionary. Change them to ints
            indices = [int(i.split(' ')[0]), int(i.split(' ')[1])]
            #Insert the value at the proper position
            matrix[indices[0], indices[1]] = value
        return matrix

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
