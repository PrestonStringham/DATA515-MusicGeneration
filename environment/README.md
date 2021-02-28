
# Conda environment #

The YAML file `env-music-gen-515.yml` specifies a Conda environment with
a number of standard packages for machine learning with Python. You can
use this file to ensure that the team is all using similar Conda
environments.

If in the course of the project, you discover packages that are needed
to move forward--and these packages are available via Conda--feel free
to add them to the YAML file.

If the packages are not available via Conda then you can document them
in this `README.md`. Also, consider creating Bash scripts for packages
not available via Conda. See the `install-*.sh` scripts in this
directory for examples.


# Set up the Conda environment `music-gen-515` #

To set up a Conda environment for our music generation project:

    conda env create -f env-music-gen.yml

To verify that the new environment was created:

    conda env list

Activate the new environment with:

    conda activate music-gen-515


# Remove the Conda environment #

Use the following commands to remove the environment:

    conda deactivate
    conda remove --name music-gen-515 --all


# The `mido` and `magenta` packages #

Use PIP to install the `mido` and `magenta` packages--if you need them.
These packages are not supported by Conda. Note that `magenta` has
numerous dependencies and will take a while to install.

    conda activate music-gen-515
    pip install mido
    pip install magenta

This directory also contains two Bash shell scripts that install these
packages:

    install-mido.sh

    install-magenta.sh


### --- END --- ###

