"""Top-level __init__.py for EasyMusicGenerator
"""

from .preprocessor.chord_distribution import (
    ChordDistribution)

from .preprocessor.note_distribution import (
    NoteDistribution, NoNotesFoundException)

from .preprocessor.preprocessor import (
    Preprocessor, NoFilesFoundException)

from .__version import __version__

__all__ = [ChordDistribution, NoNotesFoundException, NoteDistribution,
           Preprocessor, NoFilesFoundException, __version__]
