# python script to fetch title from webpage
import urllib2

def fetch_title(html, begin, end) :
	""" parse the html file to get title """
	idx1 = html.find(begin)
	idx2 = html.find(end, idx1)
	return html[idx1+len(begin):idx2].strip()

f = open("url.txt", "r")
url = f.read()
response = urllib2.urlopen(url)
html = response.read()
title = fetch_title(html, '<title>', '</title>')
print title
