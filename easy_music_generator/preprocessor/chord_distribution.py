import music21 as mus


class ChordDistribution:
    '''
    This class has methods that generate information about chord statistics.
    '''

    def __init__(self):
        pass

    @staticmethod
    def get_chord_matrix(scores):
        '''
        This method takes a list of scores as input.
        The output is a matrix with the probability of chords occuring.

        OUTPUT: chord matrix
        '''
        chord_dictionary = {}
        chord_arr = []
        for score in scores:
            chords = []
            # If a file has chords, analyze those
            elements = score.flat.elements
            for i in range(len(elements)):
                if isinstance(elements[i], mus.chord.Chord):
                    pitches = elements[i].pitches
                    chords.append(str([pitch.midi for pitch in pitches]))
            # If a file does not have chords,
            # try to chordify the files and analyze again
            # This conditional should fail
            # if a file does have at least one chord
            if(len(chords) == 0):
                chorded = score.chordify()
                elements = chorded.flat.elements
                for i in range(len(elements)):
                    if isinstance(elements[i], mus.chord.Chord):
                        pitches = elements[i].pitches
                        chords.append(str([pitch.midi for pitch in pitches]))
            chord_arr = chord_arr + chords

        # Raise exception if no chords found
        if len(chord_arr) == 0:
            raise NoChordsFoundException()

        # The chord_arr has been filled.
        # Let's get the pairs and individual chords in their own dictionary
        for i in range(len(chord_arr)):
            if str(chord_arr[i]) in chord_dictionary:
                chord_dictionary[str(chord_arr[i])] += 1
            else:
                chord_dictionary[str(chord_arr[i])] = 1

        chord_distribution = ChordDistribution.get_chord_probabilities(
            chord_dictionary)
        return chord_distribution

    @staticmethod
    def get_chord_probabilities(dictionary):
        '''
        This method takes a dictionary as input. {chord : number of occurences}
        The output is a dictionary with the probabilities of chords.

        OUTPUT: {chord : probability}
        '''
        total = sum(dictionary.values())
        for key in dictionary.keys():
            dictionary[key] /= total
        return dictionary


class NoChordsFoundException(Exception):

    '''
    This is an exception class that will be invoked when there
    no MIDI or MusicXML in the input folder.

    It will also be triggered when there are no chords in the Score object.
    '''
    def __init__(self, message="The provided MIDI or MusicXML files do not contain any chords."):
        self.message = message
        super().__init__(self.message)
