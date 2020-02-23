#!/bin/bash

contestFolder=$(pwd)
problemDirectories=(`ls`)

for directory in problemDirectories
do
    cd ${contestFolder}/${directory}
    rm *.txt
    mv a.cpp ${contestFolder}/${directory}.cpp
done