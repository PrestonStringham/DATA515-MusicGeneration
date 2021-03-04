import Preprocessor as pp
import Pregenerator as pg
#import Generator as gen

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
        preg = pg.Pregenerator()
        primer_melody = preg.generate_primer_melody(note_matrix, self.bars)
        print(primer_melody)
