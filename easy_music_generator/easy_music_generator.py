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
        print(type(primer_string))
        for i in primer_string:
            print(type(i))
       
        backing_chords = preg.generate_backing_chords(chord_matrix, self.bars)
        backing_chords_str = ""
        for chord in backing_chords:
            backing_chords_str += chord + " "
        BUNDLE_PATH = 'chord_pitches_improv.mag'
        CONFIG = 'basic_improv'
        command = f'improv_rnn_generate --config={CONFIG} --bundle_file={BUNDLE_PATH} --output_dir=/temp --num_outputs=10 --primer_melody="[56, 64, 40]" --backing_chords="A D G E" --render_chords'

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print (process.returncode)
