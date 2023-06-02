fh = open("shop.txt")
item = input("Check for what?: ")
  
print("*******************")
print("**** Checking  ****")
print("** User defined ***")
print("***** item ********")
print("***** exists ******")
print("******** ? ********")

print ('user defined word is: ', item)
data = fh.readlines()   #reading each line separately

for line in data:
	if item in line.rstrip():			#case sensitive search
		print ("line found: ", line)
else:
	print('All file is parsed')		

