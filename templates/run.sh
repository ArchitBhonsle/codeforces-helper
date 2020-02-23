#!/bin/bash

sol=$1
inpFiles=(`ls inp_*.txt`)

for ((i=0; i<${#inputFiles[@]}; ++i)); do
    ./$sol < inp_$i.txt > out_$i.txt
done