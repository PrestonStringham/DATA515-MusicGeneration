import music21 as mus
import numpy as np
import sys

class NoteDistribution:

    def __init__(self):
        pass

    @staticmethod
    def get_note_matrix(scores):
        # Dictionary to store probabilites of neighboring notes
        dictionary = {}
        note_dictionary = {}
        # iterate through all the scores
        for score in scores:

            # The actual list of notes
            notes = score.flat.notes
            itr = iter(range(len(notes) - 1))
            # Iterate through all the notes
            for i in itr:
                # Make sure all the notes are ACTUALLY notes...
                if not isinstance(notes[i], mus.note.Note) or not \
                        isinstance(notes[i+1], mus.note.Note):
                    continue
                # Create pairs of notes that will later be parsed
                # for stochastic matrix
                pair = str(notes[i].pitch.midi) + " " \
                    + str(notes[i+1].pitch.midi)

                # Add them to the dictionary
                if pair in dictionary:
                    dictionary[pair] += 1
                else:
                    dictionary[pair] = 1

                if str(notes[i].pitch.midi) in note_dictionary:
                    note_dictionary[str(notes[i].pitch.midi)] += 1
                else:
                    note_dictionary[str(notes[i].pitch.midi)] = 1

            # Get the very last note since we miss it in the loop above
            if notes[len(notes)-1].pitch.midi in note_dictionary:
                note_dictionary[str(notes[len(notes) - 1].pitch.midi)] += 1
            else:
                note_dictionary[str(notes[len(notes) - 1].pitch.midi)] = 1
            # Check if the notes are actually being added to the dictionary
            # We could have issues if a file ONLY has chords
            if len(dictionary.keys()) == 0:
                raise NoNotesFoundException()

            note_dictionary_probability = \
                NoteDistribution.get_note_probabilities(note_dictionary)
            stochastic_matrix = \
                NoteDistribution.get_stochastic_note_matrix(dictionary)

        return (stochastic_matrix, note_dictionary_probability)

    @staticmethod
    def get_stochastic_note_matrix(distribution):
        # 128 total MIDI notes
        size = 128

        # Create matrix of 128x128, one row and column for each MIDI note
        matrix = np.zeros((size, size), dtype=float)
        for i in distribution.keys():
            value = distribution[i]
            # MIDI note values were kept as strings in the dictionary.
            # Change them to ints
            indices = [int(i.split(' ')[0]), int(i.split(' ')[1])]
            # Insert the value at the proper position
            matrix[indices[0], indices[1]] = value
        for i in range(len(matrix[0, ])):
            sum_count = sum(matrix[i, ])
            for j in range(len(matrix[0, ])):
                if sum_count != 0:
                    matrix[i, j] = np.divide(matrix[i, j], sum_count)
        return matrix

    @staticmethod
    def get_note_probabilities(distribution):
        total = sum(distribution.values())
        for key in distribution.keys():
            distribution[key] /= total
        return distribution


class NoNotesFoundException(Exception):
    def __init__(self, message="The provided MIDI or MusicXML "
                 "files do not contain any notes."):
        self.message = message
        super().__init__(self.message)
