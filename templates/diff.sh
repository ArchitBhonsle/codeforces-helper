#!/bin/bash

sol=$1
expFiles=(`ls exp_*.txt`)
outFiles=(`ls out_*.txt`)

for ((i=0; i<${#outputFiles[@]}; ++i)); do
    diff -c out_$i.txt exp_$i.txt
done
