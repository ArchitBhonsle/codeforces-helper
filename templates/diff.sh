#!/bin/bash

outFiles=(`ls *.out`)

for ((i=0; i<${#outFiles[@]}; ++i)); do
    diff -c $i.out $i.exp
done
