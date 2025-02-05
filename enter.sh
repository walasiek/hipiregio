#!/bin/bash

# Run to create virtualenv for this repo
# If virtualenv is already created then activate it
# Params:
#   none

ENV_DIRNAME=hipiregio
VIRTUALENV_DIR=$HOME/virtualenv/$ENV_DIRNAME

if [[ ! -d $VIRTUALENV_DIR ]]; then
    virtualenv -p python3 $VIRTUALENV_DIR
    source $VIRTUALENV_DIR/bin/activate
    pip install -r requirements.txt

    # add virtualenv to jupyter
    python -m ipykernel install --user --name=$ENV_DIRNAME
    echo "Please set up your password to jupyter for easier usage:"
    jupyter notebook password
else
    export PYTHONPATH=$PYTHONPATH:`pwd`
    source $VIRTUALENV_DIR/bin/activate
fi
