
![Travis (.org)](https://img.shields.io/travis/PrestonStringham/DATA515-MusicGeneration)

This repository contains our team project for Data 515 in the University
of Washington Masters in Data Science program.

The requirements for the project are described [here][project-info]
[access required].


# Installation #

**NOTE:** Installation of some of the packages required for
**EasyMusicGenerator** can take significant time. The install process
described here can take 30+ minutes.

Next, clone this repository to your local computer.

    git clone https://github.com/PrestonStringham/DATA515-MusicGeneration

Change directories to the local copy of the repository.

    cd DATA515-MusicGeneration

The `pip` installer has difficulty installing some Python packages used
for data science. We recommend that you create a custom conda
environment using the provided `env-music-gen.yml` file.

    conda env create -f env-music-gen.yml
                                                           
Activate the newly created conda environment, `music-gen-515`.

    conda activate music-gen-515 


    
Install the package--and remaining package requirements--using the
following PIP command line.

    pip install .

If after using **EasyMusicGenerator**, you'd like to remove the
recommended conda environment, use the following commands.

    conda activate
    conda remove --name music-gen-515 --all

Verify removal.

    conda env list


[project-info]:https://canvas.uw.edu/courses/1434044/pages/project-infomation


# Usage #

Make sure that you are inside the DATA515-MusicGeneration directory before running the following code.

```python 
from easy_music_generator import easy_music_generator as emg
emg_obj = emg.EasyMusicGenerator()
input_file_path = 'easy_music_generator/music/'
emg_obj.analyze(input_file_path)
output_file_path = 'output/'
number_of_bars = 10
emg_obj.generate(number_of_bars, output_file_path)
```

This code is also available in `examples/example.py`, but your must be
in the `examples` directory in order to run that file.


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
          

# DATA

We trained our model on a segment of [the Lakh MIDI Dataset](https://colinraffel.com/projects/lmd/). 

The Lakh MIDI Dataset is distributed with a CC-BY 4.0 license. 

Colin Raffel. "Learning-Based Methods for Comparing Sequences, with Applications to Audio-to-MIDI Alignment and Matching". PhD Thesis, 201. 


# MODEL 

We used [Magenta's Polyphony RNN](https://github.com/magenta/magenta/tree/master/magenta/models/polyphony_rnn). 


### --- END --- ###
