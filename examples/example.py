import sys
sys.path.append('../')
from easy_music_generator import easy_music_generator as emg

emg_obj = emg.EasyMusicGenerator()

emg_obj.analyze('music/')
emg_obj.generate(10, 'output/')
