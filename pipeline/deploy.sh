#!/bin/bash

echo "This is a script to run on a Deploy"

virtualenv venv
pwd
source ./venv/bin/activate
sudo pip install -r requirements.txt --ignore-installed
wget https://github.com/jgraham/wires/releases/download/v0.6.2/wires-0.6.2-linux64.gz /home/contint/workspace/vdc/portalesnovdc/
gzip -d /home/contint/workspace/vdc/portalesnovdc/wires-0.6.2-linux64.gz
export PATH=$PATH:/home/contint/workspace/vdc/portalesnovdc/
