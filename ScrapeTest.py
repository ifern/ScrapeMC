import urllib
import io
import re

#wordsfile = csv.DictReader(open("words.csv"))


#Search for every word in the words list in every URL in the links list. Print both word and the URL if found

#for word in wordsfile:
#	curr_word = word['search_word']

#	linksfile = csv.DictReader(open("links.csv"))

#	for link in  linksfile:
#		curr_link = link['url']
#		site = urllib.urlopen(curr_link).read()

#        	if curr_word in site:

#define the URL to be accessed and the word to be searched
curr_link = 'http://www.myiris.com/shares/research/researchHome.php?yesdate=1&more=1&iStart=0&alpha='
curr_word = '29-JUN-15'

#read the html into a string
site = urllib.urlopen(curr_link).read()

#store the html is a file
text_file = open("Output.txt", "w")
text_file.write(site)
text_file.close()

#open the file in read mode
f = open("Output.txt",'r')

#read every line of html and search for the keyword
for line in f:
	if re.search(curr_word,line):
		print(line)
