import re
# You must have an input file named shop.txt

fh = open("/Users/valentinaronchi/Desktop/school/uni/first year/web development/practical/week6/shop.txt")

for line in fh:
  #replace e with z
  line = line.rstrip('\n')
  line = line.replace('e','z') 
  print(line)
fh.close()

print("*******************")
print("*** Another Way ***")
print("*******************")
print("****** Using ******")
print("**** re Module ****")
print("*******************")

fh = open("/Users/valentinaronchi/Desktop/school/uni/first year/web development/practical/week6/shop.txt")
for line in fh:
  line = re.sub('e','z',line)
  print(line.rstrip('\n'))  
fh.close()
  

print("*******************")
print("*** Another Way ***")
print("*******************")
print("****** Using ******")
print("**** read func ****")
print("*******************")

fh = open("/Users/valentinaronchi/Desktop/school/uni/first year/web development/practical/week6/shop.txt")
data = fh.read()	# no use of loop
data = data.replace('e','z')
print (data)
fh.close()

fh = open("/Users/valentinaronchi/Desktop/school/uni/first year/web development/practical/week6/shop.txt")
data = fh.read()	# no use of loop
data = data.replace('a','b')
print (data)
fh.close()

