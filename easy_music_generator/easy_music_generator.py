import preprocessor.preprocessor as pp
import pregenerator as pg
import subprocess

class EasyMusicGenerator:

    def __init__(self, tempo, bars, path, output_format):
        self.tempo = tempo
        self.bars = bars
        self.path = path
        self.output_format = output_format

    def generate(self):
        prep = pp.Preprocessor()
        scores_parsed = prep.parse_scores(self.path)
        note_matrix = prep.get_note_matrix()
        chord_matrix = prep.get_chord_matrix()
        preg = pg.Pregenerator()
        primer_melody = preg.generate_primer_melody(note_matrix, self.bars) 
        #primer_string = ", ".join(primer_melody)
        
        primer_string = str(primer_melody)
        backing_chords = preg.generate_backing_chords(chord_matrix, self.bars)
        backing_chords_str = ""
        for chord in backing_chords:
            backing_chords_str += chord + " "
       
        BUNDLE_PATH = 'polyphony_rnn.mag'

        command = f'polyphony_rnn_generate --bundle_file={BUNDLE_PATH}​​​​ --output_dir=/tmp/polyphony_rnn/generated2 --num_outputs=10 --num_steps=128 --primer_melody={primer_string}​​​​ --condition_on_primer=true --inject_primer_during_generation=false'

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print (process.returncode)
