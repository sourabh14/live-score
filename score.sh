#!/bin/bash
# bash script to redirect output of python script
# to notify-send

logopath=`pwd`;
logopath="$logopath/logo.jpg"
while true
do 
	python score.py | while read OPT; do notify-send -i "$logopath" "$OPT"; done
	sleep 20		
	#generate notif every 20 sec
done
