#!/bin/bash

echo "This is a script to run on a acceptanceTest"
ls -la *
pwd
source ./venv/bin/activate
export DISPLAY=:1
xvfb-run behave tests/web
