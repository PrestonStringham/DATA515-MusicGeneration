import preprocessor.preprocessor as pp
import pregenerator as pg
import subprocess
from subprocess import DEVNULL, STDOUT  # , check_call
# import os


class EasyMusicGenerator:

    def __init__(self):
        self.note_matrix = None
        self.chord_distribution = None

    filepath = '/music_generator_output'

    def generate(self, tempo=90, bars=4, output_path=filepath):
        preg = pg.Pregenerator()
        primer_melody = preg.generate_primer_melody(self.note_matrix, bars)
        primer_string = '['
        for i in range(len(primer_melody)):
            primer_string += str(primer_melody[i]) + ', '
        primer_string += str(primer_melody[len(primer_melody)-1])
        primer_string += ']'

        backing_chord = preg.generate_backing_chords(self.chord_distribution,
                                                     bars)

        backing_string = '['
        for i in range(len(backing_chord)):
            backing_string += str(backing_chord[i]) + ', '
        backing_string += str(backing_string[len(backing_string)-1])
        backing_string += ']'

        # backing_string = ' '.join(backing_chords)
        BUNDLE_PATH = "lakh2_polyphony_rnn.mag"

        OUTPUT_PATH = output_path

        # 16 steps in a bar
        num_steps = str(16*bars)

        command = 'polyphony_rnn_generate --bundle_file=' +\
                  BUNDLE_PATH + ' --output_dir=' + OUTPUT_PATH +\
                  ' --num_outputs=1 --num_steps=' + num_steps +\
                  ' --primer_melody="' + primer_string +\
                  '" --primer_pitches="' + backing_string +\
                  '" --condition_on_primer=true ' \
                  '--inject_primer_during_generation=false'
        command = f'{command}'

        process = subprocess.Popen(command, shell=True,
                                   stdout=DEVNULL, stderr=STDOUT)
        process.wait()

    def analyze(self, input_path):
        prep = pp.Preprocessor()
        scores_parsed = prep.parse_scores(input_path)
        note_matrix = prep.get_note_matrix()
        chord_distribution = prep.get_chord_matrix()
        self.note_matrix = note_matrix
        self.chord_distribution = chord_distribution
