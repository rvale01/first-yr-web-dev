inFile = "/Users/valentinaronchi/Desktop/school/uni/first year/web development/practical/week6/shop.txt"   #shop.txt is already in the folder
# You must have an input file
fh = open(inFile)  # opening a file in read mode

# loop over input file
for line in fh:
	print ("** ", line.rstrip('\n'))
	
  



