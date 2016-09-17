#!/bin/bash

pyuic5 design.ui -o design.py

# sudo zypper in python3-pyflakes
# check code
pyflakes *.py

# sudo zypper in python3-pylint python3-wrapt
# http://stackoverflow.com/questions/31907762/pylint-to-show-only-warnings-and-errors
#pylint main.py
#pylint --disable=R,C,W *.py
