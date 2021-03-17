import numpy as np


class Pregenerator:
    '''
    This class has methods to generate the primers.
    Primers include primer melody and primer backing chords.
    These primers will serve as input for the RNN model to generate more music.

    '''
    def __init__(self):
        self.primer_melody = None
        self.backing_chords = None

    def generate_primer_melody(self, matrix_tuple, bars):
        '''
        This method generates our primer melody by
        implementing a one-step Markov chain.
        INPUTS:
        matrix_tuple: tuple containing:
            - a matrix with notes probabililties (for note interactions)
            - a dictionary with single note probabilities
        bars: number of bars (length of music)
        OUTPUT: array with notes
        example: [60, -2, 60, -2]
        '''
        primer_melody_arr = []
        matrix = matrix_tuple[0]
        dictionary = matrix_tuple[1]
        notes = list(dictionary.keys())
        note_probability = list(dictionary.values())
        # selecting first note randomly
        # probability of note defined based on songs from user input
        first_note = int(np.random.choice(notes, p=note_probability))
        primer_melody_arr.append(first_note)
        current_note = first_note

        # Based on previous note, select next note
        for i in range(bars - 1):
            primer_melody_arr.append(np.random.choice([-1, -2]))
            next_note = np.random.choice(a=range(128),
                                         p=matrix[current_note, ])
            primer_melody_arr.append(next_note)
            current_note = next_note

        return primer_melody_arr

    def generate_backing_chords(self, chord_dictionary, bars):
        '''
        This method generates the primer chord
        to be used as input by Polyphony RNN.

        INPUT:
        chord_dictionary: dictionary with chords
        and probability. {chord: probability}


        OUTPUT: a string representing a chord
        example: '[55, 76]' # chord composed of 2 MIDI notes
        '''
        chords = list(chord_dictionary.keys())
        chord_probability = list(chord_dictionary.values())
        first_chord_index = int(np.random.choice(a=range(len(chords)),
                                                 p=chord_probability))
        first_chord = chords[first_chord_index]

        return first_chord
