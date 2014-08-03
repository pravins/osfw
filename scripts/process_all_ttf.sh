#!/bin/sh

all_ttf=`find /usr/share/fonts -name "*.ttf"`
#for generating binary tar ball
for s in $all_ttf
do
#echo "processing"
echo $s
python osfw-getting-font-info.py $s
done

