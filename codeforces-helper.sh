#!/bin/bash

source "${CFHVENV}/activate"
python "${CFHDIR}/main.py" $1
# * CFHVENV is the environment variable to the virtual-env that has bs4 and requests
# * CFHDIR is the path where codeforces-helper is cloned
# ! YOURS WILL BE DIFFERENT

cd $DIRFORCES