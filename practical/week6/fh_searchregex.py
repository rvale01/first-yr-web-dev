import re

fh = open('animals.txt')
search = r"rat"

for line in fh:
	if re.search(search, line, re.IGNORECASE) != None:
		print (line)



