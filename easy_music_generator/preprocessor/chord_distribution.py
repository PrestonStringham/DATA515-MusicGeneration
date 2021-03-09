import music21 as mus
import numpy as np

class ChordDistribution:

    def __init__(self):
        pass

    @staticmethod
    def get_chord_matrix(scores):
        pair_dic = {}
        dic = {}
        chord_arr = []
        for score in scores:
            chords = []
            #If a file has chords, analyze those
            elements = score.flat.elements
            for i in range(len(elements)):
                if isinstance(elements[i], mus.chord.Chord):
                    if mus.harmony.chordSymbolFigureFromChord(elements[i]) != 'Chord Symbol Cannot Be Identified':
                        chords.append(mus.harmony.chordSymbolFigureFromChord(elements[i]))
            #If a file does not have chords, try to chordify the files and analyze again
            #This conditional should fail if a file does have at least one chord
            if(len(chords) == 0):
                chorded = score.chordify()
                elements = chorded.flat.elements
                for i in range(len(elements)):
                    if isinstance(elements[i], mus.chord.Chord):
                        #You NEED to check for 'Chord Symbol Cannot Be Identified' twice here. Not entirely sure
                        #why the first conditional doesn't catch everything
                        if mus.harmony.chordSymbolFigureFromChord(elements[i]) != 'Chord Symbol Cannot Be Identified':
                            if mus.harmony.chordSymbolFigureFromChord(elements[i]) != 'Chord Symbol Cannot Be Identified':
                                chords.append(mus.harmony.chordSymbolFigureFromChord(elements[i]))
            chord_arr = chord_arr + chords
        if len(chord_arr) == 0:
            raise NoChordsFoundException()
        #The chord_arr has been filled. Let's get the pairs and individual chords in thier own dictionary
        for i in range(len(chord_arr) - 1):
            pair = str(chord_arr[i]) + ' ' + str(chord_arr[i+1])
            if pair in dic:
                pair_dic[pair] += 1
            else:
                pair_dic[pair] = 1

            if str(chord_arr[i]) in dic:
                dic[str(chord_arr[i])] += 1
            else:
                dic[str(chord_arr[i])] = 1
        matrix, matrix_dictionary = ChordDistribution.get_stochastic_matrix(pair_dic, dic)
        chord_distribution = ChordDistribution.get_chord_probabilities(dic)
        return (matrix, matrix_dictionary, chord_distribution)

    @staticmethod
    def get_stochastic_matrix(pairs, singles):
        pair_keys = list(pairs.keys())
        single_keys = list(singles.keys())
        pair_size = len(pair_keys)
        single_size = len(single_keys)
        dic = {}
        for i in range(single_size):
            dic[single_keys[i]] = i
        matrix = np.zeros((single_size, single_size), dtype=float)
        for i in range(pair_size):
            value = pairs[pair_keys[i]]
            chord_split = [pair_keys[i].split(' ')[0], pair_keys[i].split(' ')[1]]
            #print(chord_split)
            matrix[dic[chord_split[0]], dic[chord_split[1]]] = value
        for i in range(len(matrix[0, ])):
            sum_count = sum(matrix[i, ])
            for j in range(len(matrix[0, ])):
                if sum_count != 0:
                    matrix[i, j] = np.divide(matrix[i, j], sum_count)
        return (matrix, dic)

    @staticmethod
    def get_chord_probabilities(dic):
        total = sum(dic.values())
        for key in dic.keys():
            dic[key] /= total
        return dic

class NoChordsFoundException(Exception):
    def __init__(self, message="The provided MIDI or MusicXML files do not contain any chords."):
        self.message = message
        super().__init__(self.message)
