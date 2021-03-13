import numpy as np
import music21 as mus

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

    def generate_backing_chords(self, chord_dictionary, bars):
        chords = list(chord_dictionary.keys())
        chord_probability = list(chord_dictionary.values())
        first_chord = mus.harmony.ChordSymbol(np.random.choice(chords, p=chord_probability)).pitches
        first_chord_array = []

        for i in first_chord:
            first_chord_array.append(i.midi)

        return first_chord_array
