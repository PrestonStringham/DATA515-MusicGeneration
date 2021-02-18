
# Conda environment #

To set up a conda environment for our music generation project:

    conda env create -f env-music-gen.yml


# The `mido` and `magenta` packages #

Use PIP to install the `mido` and `magenta` packages--if you need them.
These packages are not supported by Conda. Note that `magenta` has
numerous dependencies and will take a while to install.

    conda activate music-gen-515
    pip install mido
    pip install magenta

This directory also contains two Bash shell scripts that will install
these packages:

    install-mido.sh

    install-magenta.sh


### --- END --- ###

