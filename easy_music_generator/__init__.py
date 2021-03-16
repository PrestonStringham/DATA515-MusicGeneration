"""Top-level __init__.py for EasyMusicGenerator
"""

from easy_music_generator.preprocessor.chord_distribution import (
    ChordDistribution)

from easy_music_generator.preprocessor.note_distribution import (
    NoteDistribution, NoNotesFoundException)

from easy_music_generator.preprocessor.preprocessor import (
    Preprocessor, NoFilesFoundException)

from .__version import __version__

__all__ = [ChordDistribution, NoNotesFoundException, NoteDistribution,
           Preprocessor, NoFilesFoundException, __version__]
