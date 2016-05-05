#!/bin/bash

echo "This is a script to run on a InstallationTest"
ls -la *
pwd
source ./bin/activate
behave --version
