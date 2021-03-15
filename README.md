
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

Install using the following PIP command line.

    pip install -e .


[project-info]:https://canvas.uw.edu/courses/1434044/pages/project-infomation


# Project Structure #

|- DATA515-MusicGeneration/

      |- doc/
      |- easy_music_generator/
         |- music/
            |-...
         |- preprocessor/ 
            |- tests
                |- _init_.py
                |- test_chord_distribution.py
                |- test_note_distribution.py
                |- test_preprocessor.py
            |- _init_.py
            |- chord_distribution.py
            |- note_distribution.py
            |- preprocessor.py
         |- tests/
            |-_init_.py
            |-test_easy_music_generator.py
         |- _init__.py
         |- __version.py
         |- easy_music_generator.py
         |- example.py
         |- pregenerator.py
         |- lakh2_polyphony_rnn.mag  
      |- .gitignore
      |- .travis.yml
      |- LICENSE
      |- README.md
      |- requirements.txt
      |- setup.py

### --- END --- ###

