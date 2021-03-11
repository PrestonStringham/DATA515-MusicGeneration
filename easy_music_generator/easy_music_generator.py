import preprocessor.preprocessor as pp
import pregenerator as pg
import subprocess
import os


class EasyMusicGenerator:

    def __init__(self, tempo, bars, path, output_path):
        self.tempo = tempo
        self.bars = bars
        self.path = path
        self.output_path = output_path

    def generate(self):
        prep = pp.Preprocessor()
        # scores_parsed = prep.parse_scores(self.path)
        note_matrix = prep.get_note_matrix()
        chord_matrix = prep.get_chord_matrix()
        preg = pg.Pregenerator()
        
        primer_melody = preg.generate_primer_melody(note_matrix, self.bars) 
        primer_string = '['
        for i in range(len(primer_melody)):
            primer_string += str(primer_melody[i]) + ', '
        primer_string += str(primer_melody[len(primer_melody)-1])
        primer_string += ']'

        backing_chords = preg.generate_backing_chords(chord_matrix, self.bars)
        backing_string = ' '.join(backing_chords)
       
        BUNDLE_PATH = "chord_pitches_improv.mag"
        OUTPUT_PATH = self.output_path

        command = 'improv_rnn_generate \
                    --config=chord_pitches_improv \
                    --bundle_file=' + BUNDLE_PATH + ' \
                    --output_dir=' + OUTPUT_PATH + ' \
                    --num_outputs=1 --primer_melody="' + primer_string + '" \
                    --backing_chords=' + str(backing_string) + ' \
                    --render_chords \
                    --num_steps=128'

        #command = f'polyphony_rnn_generate \
        #           --bundle_file={BUNDLE_PATH} \
        #           --output_dir=/tmp/polyphony_rnn/generated2 \
        #           --num_outputs=10 \
        #           --num_steps=128 \
        #           --primer_melody={primer_string}​​​​ \
        #           --condition_on_primer=true \
        #           --inject_primer_during_generation=false'
        
        command = f'{command}'

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print (process.returncode)
