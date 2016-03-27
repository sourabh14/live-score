#!/usr/bin/python
from Window import *
import re
import time
import urllib2
import os

# create GuiWindow object
windowinput = GuiWindow()

# fetch input
url = windowinput.url
interval = windowinput.interval	
notifOption = windowinput.notifChoice

# start live score
print "url : ", url
print "interval : ", interval
print "selection : ", notifOption
print "\nrunning live-score...\n\n"


def fetch_title(html, begin, end) :
	""" parse the html file to get title """
	idx1 = html.find(begin)
	idx2 = html.find(end, idx1)
	return html[idx1+len(begin):idx2].strip()


prevRuns = 0
prevWkts = 0
logoPath = os.getcwd() + "/logo.jpg"
notifCmd = "notify-send -i " + logoPath + " "


# After every interval
if (windowinput.notifChoice == 1):			
	while(True):
		# fetch title from url
		response = urllib2.urlopen(url)
		html = response.read()
		title = fetch_title(html, '<title>', '</title>')	

		# show notification
		command = notifCmd + "\"" + title + "\""
		os.system(command)

		# give delay	
		time.sleep(interval) 	


# When runs are scored
elif (windowinput.notifChoice == 2):		
	while(True):
		# fetch title from url
		response = urllib2.urlopen(url)
		html = response.read()
		title = fetch_title(html, '<title>', '</title>')	

		# fetch runs
		obj = re.search(r'(\d+)/(\d+)', title)
		runs = obj.group(1)
		wkts = obj.group(2)

		# show notification only when runs are scored
		if (runs != prevRuns):
			prevRuns = runs
			command = notifCmd + "\"" + title + "\""
			os.system(command)
		else:
			print "runs not scored.."	

		# give delay	
		time.sleep(interval) 

# When wickets fall
else:					
	while(True):
		# fetch title from url
		response = urllib2.urlopen(url)
		html = response.read()
		title = fetch_title(html, '<title>', '</title>')	

		# fetch runs
		obj = re.search(r'(\d+)/(\d+)', title)
		runs = obj.group(1)
		wkts = obj.group(2)

		# show notification only when runs are scored
		if (wkts != prevWkts):
			wkts = prevWkts
			command = notifCmd + "\"" + title + "\""
			os.system(command)
		else:
			print "wkts not fallen.."	

		# give delay	
		time.sleep(interval) 					