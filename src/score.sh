#!/bin/bash
# bash script to redirect output of python script
# to notify-send

logopath=`pwd`
logopath="${logopath//src/images/logo.jpg}"
# echo "logopath : $logopath"

echo "Enter url : "
read ur
echo "$ur" > url.txt

while true
do 
	python score.py | while read OPT; do notify-send -i "$logopath" "$OPT"; done
	sleep 30	
	#generate notification every 30 sec
done
