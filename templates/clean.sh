#!/bin/bash

source "${CFHVENV}/activate"
contestDirectory=`pwd`
python "${CFhDIR}/clean.py" ${contestDirectory}

# * CFHVENV is a environment variable to the virtual-env that has bs4 and requests
# * CFHDIR is a path where codeforces-helper is cloned