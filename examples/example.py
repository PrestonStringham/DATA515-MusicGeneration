from easy_music_generator import easy_music_generator as emg
import sys
sys.path.append('../')

emg_obj = emg.EasyMusicGenerator()

emg_obj.analyze('music/')
emg_obj.generate(10, 'output/')
