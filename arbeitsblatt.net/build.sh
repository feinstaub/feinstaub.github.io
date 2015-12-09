#!/bin/bash

# For syntax-highlighting
# sudo zypper install source-highlight

# AsciiDoc ships with two themes: flask and volnitsky.
asciidoc -b html5 -a icons -a toc2 -a --theme=flask *.adoc
