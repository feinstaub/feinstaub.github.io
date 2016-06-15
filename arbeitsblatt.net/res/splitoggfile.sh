#!/bin/bash

mkdir _out
cd _out

cp /usr/share/kde4/apps/amarok/data/first_run_jingle.ogg .

echo
echo "### split ###"
echo
mp3splt first_run_jingle.ogg -c ../splitoggfile.cue

echo
echo "### list ###"
echo
ls -la

echo
echo "### ogginfo ###"
echo
ogginfo Artist\ 1\ -\ 1\ -\ Part\ 1.ogg
