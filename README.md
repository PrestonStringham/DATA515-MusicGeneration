
![Travis (.org)](https://img.shields.io/travis/PrestonStringham/DATA515-MusicGeneration)

This repo is our team project for Data 515 in the University of
Washington Masters in Data Science program.

The requirements for the project are described [here][project-info]
[access required].


# Installation #

Clone this repository to your local computer.

    git clone https://github.com/PrestonStringham/DATA515-MusicGeneration

Change directories to the local copy of the repo.

    cd DATA515-MusicGeneration
    
Activate a base anaconda environment.
 
    conda activate

Install using the following PIP command line.

    pip install .


[project-info]:https://canvas.uw.edu/courses/1434044/pages/project-infomation


# Usage #

Make sure that you are inside the DATA515-MusicGeneration directory before running the following code.

```python 
from easy_music_generator import easy_music_generator as emg
emg_obj = emg.EasyMusicGenerator()
input_file_path = 'music/'
emg_obj.analyze(input_file_path)
output_file_path = 'output/'
number_of_bars = 10
emg_obj.generate(number_of_bars, output_file_path)
```

# Project Structure #

    |- DATA515-MusicGeneration/
          |.vscode
          |- doc/
            |-...
          |- easy_music_generator/
             |- music/
                |-...
             |- preprocessor/
                |- tests
                    |- __init__.py
                    |- test_chord_distribution.py
                    |- test_note_distribution.py
                    |- test_preprocessor.py
                |- __init__.py
                |- chord_distribution.py
                |- note_distribution.py
                |- preprocessor.py
             |- tests/
                |-__init__.py
                |-test_easy_music_generator.py
             |- __init__.py
             |- __version.py
             |- easy_music_generator.py
             |- pregenerator.py
             |- lakh2_polyphony_rnn.mag  
          |- examples
            |- music
                |- ...
            |- example.py
            |- example_notebook.ipynb
          |- tests
            |- emg-import-test.py
          |- .gitignore
          |- .travis.yml
          |- LICENSE
          |- README.md
          |- requirements.txt
          |- setup.py

### --- END --- ###
