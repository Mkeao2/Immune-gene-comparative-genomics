#!/bin/bash

for i in Genometest/*.zip; 
do unzip *.zip -d *.txt  ;     
datasets/datasets2 rehydrate --directory */;
zip -r *.zip 
rm */* 
rmdir *;
done
