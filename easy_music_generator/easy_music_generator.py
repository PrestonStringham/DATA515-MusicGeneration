from easy_music_generator.preprocessor import preprocessor as pp
import easy_music_generator.pregenerator as pg
import subprocess
import os
from subprocess import DEVNULL


class EasyMusicGenerator:
    '''
    This is the main class. It contains two methods: generate and analyze.
    This class calls other helper classes: preprocessor and pregenerator.
    '''
    def __init__(self):
        self.note_matrix = None
        self.chord_distribution = None

    filepath = '/music_generator_output'

    def generate(self, bars=4, output_path=filepath):
        '''
        This method uses the instantiated matrices
        from analyze() to generate music.
        bars: length of the music
        output_path: path to the directory where to output MIDI file

        First stage:
        Pregenerator to generate primer melody and primer chord (pitches).

        Second stage:
        Use primers as input and generate more music using polyphony_rnn.

        OUTPUT: MIDI file
        '''
        # First Stage: Generate primers
        preg = pg.Pregenerator()
        primer_melody = preg.generate_primer_melody(self.note_matrix, bars)
        primer_string = '['
        for i in range(len(primer_melody)):
            primer_string += str(primer_melody[i]) + ', '
        primer_string += str(primer_melody[len(primer_melody)-1])
        primer_string += ']'

        backing_chord = preg.generate_backing_chords(self.chord_distribution,
                                                     bars)

        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Second stage: Generate music using Polyphony RNN
        # Polyphony RNN model trained on segment of Lakh MIDI
        BUNDLE_PATH = dir_path + "/lakh2_polyphony_rnn.mag"

        OUTPUT_PATH = output_path

        # 16 steps in a bar
        num_steps = str(16*bars)

        command = 'polyphony_rnn_generate --bundle_file=' +\
                  BUNDLE_PATH + ' --output_dir=' + OUTPUT_PATH +\
                  ' --num_outputs=1 --num_steps=' + num_steps +\
                  ' --primer_melody="' + primer_string +\
                  '" --primer_pitches="' + backing_chord +\
                  '" --condition_on_primer=true ' \
                  '--inject_primer_during_generation=false'
        try:
            command = f'{command}'
            process = subprocess.Popen(command, shell=True,
                                       stdout=DEVNULL, stderr=DEVNULL)

            process.wait()
            print('Generated successfully!')
        except Exception:
            print('Error. File not generated successfully.')

    def analyze(self, input_path):
        '''
        This method takes a directory with
        MIDI or MusicXML files.
        It instantiates two matrices: note distribution
        matrix and chord distribution.
        These matrices will be used to generate
        music in the generate() method.
        '''
        prep = pp.Preprocessor()
        prep.parse_scores(input_path)
        note_matrix = prep.get_note_matrix()
        chord_distribution = prep.get_chord_matrix()
        self.note_matrix = note_matrix
        self.chord_distribution = chord_distribution
