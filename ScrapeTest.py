import urllib
import csv
import requests
import io
import re
import sys

wordsfile = csv.DictReader(open("words.csv"))


#Search for every word in the words list in every URL in the links list. Print both word and the URL if found

for word in wordsfile:
	curr_word = word['search_word']

	linksfile = csv.DictReader(open("links.csv"))

	for link in  linksfile:
		curr_link = link['url']
		site = urllib.urlopen(curr_link).read()

        	if curr_word in site:
			text_file = open("Output.txt", "w")
			text_file.write(site)
			text_file.close()
	f = open("Output.txt",'r')
	
	for line in f:
		if re.search(curr_word,line):
			print(line)
