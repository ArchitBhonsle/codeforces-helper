#!/bin/bash

inpFiles=(`ls *.inp`)

for ((i=0; i<${#inpFiles[@]}; ++i)); do
    ./sol < $i.inp > $i.out
done