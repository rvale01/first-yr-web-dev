mystring = "Python under Linux is great"
mylist = ['a', 'b', 3, 4]    # list
mytuple = ('a', 'b', 3, 4)    # tuple
mymarks = {"webProg":80, "OOSD":70, "POC":68, "NOS": 50}   # sequence
myset = set("this is a book")

#list operations - check lecture slides
print(mylist)
mylist.insert(2,'c')
mylist.append(5)
print(mylist)
print(mylist[::-1])
mylist.pop()

if "c" in mylist:
  print("Yes")

mylist2 = []
mylist2 = mylist
print(mylist2)

#typle operations - check lecture slides
print(mytuple[0])
print(mytuple[1])
mytuple= mytuple+ (2, )
print(mytuple)
mytuple = list(mytuple)
mytuple.pop()
mytuple = tuple(mytuple)
print(mytuple)


#string operations - check lecture slides
print (mystring[::3])
print (mystring[::4])
mystring = mystring + " Hi"
print(mystring)
print(len(mystring))
print(mystring*3)

#dictionary operations - check lecture slides
print(mymarks['webProg'])
print(mymarks.keys())
print(mymarks.values())
mymarks['webProg'] = 100
print(mymarks['webProg'])
print('\n')
modulecode = {"webProg":"UFC80", "OOSD":"UFC70", "POC":"UFC68", "NOS": "UFC50"}
staff = {"Zaheer":"3Q31", "Julia":"2P35", "Rong":"2P35", "Martin":"2P21"}
course = {"module": modulecode, "staff": staff}
print (course["staff"]["Julia"])
print (course["module"]["webProg"])

for key in mymarks.keys():
  print("Key: ", key, " Value: ", mymarks[key]) 

#set operations - check lecture slides
print(myset)


