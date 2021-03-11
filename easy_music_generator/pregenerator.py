import numpy as np


class Pregenerator:
    def __init__(self):
        self.primer_melody = None
        self.backing_chords = None

    def generate_primer_melody(self, matrix_tuple, bars):
        primer_melody_arr = []
        matrix = matrix_tuple[0]
        dictionary = matrix_tuple[1]
        notes = list(dictionary.keys())
        note_probability = list(dictionary.values())
        first_note = int(np.random.choice(notes, p=note_probability))
        primer_melody_arr.append(first_note)
        current_note = first_note

        for i in range(bars - 1):
            primer_melody_arr.append(np.random.choice([-1, -2]))
            next_note = np.random.choice(range(128), p=matrix[current_note, ])
            primer_melody_arr.append(next_note)
            current_note = next_note

        return primer_melody_arr

    def generate_backing_chords(self, chord_tuple, bars):
        backing_chords_arr = []
        matrix = chord_tuple[0]
        matrix_dictionary = chord_tuple[1]
        chord_dic = chord_tuple[2]
        chords = list(chord_dic.keys())
        chord_probability = list(chord_dic.values())
        first_chord = np.random.choice(chords, p=chord_probability)
        backing_chords_arr.append(first_chord)
        current_chord = matrix_dictionary[first_chord]
        for i in range((bars - 1)*4):
            next_chord = chords[matrix_dictionary[np.random.choice(chords, p=matrix[current_chord])]]
            backing_chords_arr.append(next_chord)
            current_chord = matrix_dictionary[next_chord]

        return backing_chords_arr
