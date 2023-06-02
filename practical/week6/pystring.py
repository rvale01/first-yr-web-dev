line = input ("Enter some text ")
print ("You gave " , len(line) , " characters")   #len() method returns number of characters in string
print(" ")
line = line.upper() # upper() method to convert string to uppercase 
					# more string methods: https://docs.python.org/3.4/library/stdtypes.html#string-methods
print ("In uppercase: ", line)
print("In lowecase: ", line.lower())

if len(line) > 5 and len(line) < 10 :
     print(" ")
     print ("More than 5 characters and less than 10")
print(" ")
print(line[::-1])
  
  

