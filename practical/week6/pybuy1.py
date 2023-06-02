fh = open("/Users/valentinaronchi/Desktop/school/uni/first year/web development/practical/week6/shop.txt")
item = input("Check for what?: ")  # do not put quotes around user input
item = item.lower()
print("*******************")
print("**** Checking  ****")
print("** User defined ***")
print("***** item ********")
print("***** exists ******")
print("******** ? ********")

print ('user defined item is: ', item)
data = fh.read()
print ("All file data is:")
print (data)

if item in data:
    print ("Item exists in shop.txt")
else:
    print ("Item does not exists in shop.txt")

