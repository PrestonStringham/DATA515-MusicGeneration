import music21 as mus
# import numpy as np


class ChordDistribution:

    def __init__(self):
        pass

    @staticmethod
    def get_chord_matrix(scores):
        chord_dictionary = {}
        chord_arr = []
        for score in scores:
            chords = []
            # If a file has chords, analyze those
            elements = score.flat.elements
            for i in range(len(elements)):
                if isinstance(elements[i], mus.chord.Chord):
                    if mus.harmony.chordSymbolFigureFromChord(elements[i])\
                            != 'Chord Symbol Cannot Be Identified':
                        chords.append(mus.harmony.chordSymbolFigureFromChord(
                            elements[i]))
            # If a file does not have chords,
            # try to chordify the files and analyze again
            # This conditional should fail
            # if a file does have at least one chord
            if(len(chords) == 0):
                chorded = score.chordify()
                elements = chorded.flat.elements
                for i in range(len(elements)):
                    if isinstance(elements[i], mus.chord.Chord):
                        # You NEED to check for 'Chord Symbol Cannot
                        # Be Identified' twice here. Not entirely sure
                        # why the first conditional doesn't catch everything
                        if mus.harmony.chordSymbolFigureFromChord(elements[i])\
                                != 'Chord Symbol Cannot Be Identified':
                            if mus.harmony.chordSymbolFigureFromChord(
                                    elements[i]) != \
                                    'Chord Symbol Cannot Be Identified':
                                chords.append(
                                    mus.harmony.chordSymbolFigureFromChord(
                                        elements[i]))
            chord_arr = chord_arr + chords
        if len(chord_arr) == 0:
            raise NoChordsFoundException()
        # The chord_arr has been filled.
        # Let's get the pairs and individual chords in their own dictionary
        for i in range(len(chord_arr) - 1):
            if str(chord_arr[i]) in chord_dictionary:
                chord_dictionary[str(chord_arr[i])] += 1
            else:
                chord_dictionary[str(chord_arr[i])] = 1

        chord_distribution = ChordDistribution.get_chord_probabilities(
            chord_dictionary)
        return chord_distribution

    @staticmethod
    def get_chord_probabilities(dictionary):
        total = sum(dictionary.values())
        for key in dictionary.keys():
            dictionary[key] /= total
        return dictionary


class NoChordsFoundException(Exception):
    def __init__(self, message="The provided MIDI or MusicXML "
                               "files do not contain any chords."):
        self.message = message
        super().__init__(self.message)
