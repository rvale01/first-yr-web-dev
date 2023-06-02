for i in (0,3+1):
  print (i, "Hello")
print("Loop ended\n")

 
for i in range(0,10):  #notice the difference with tuple and range().
  print (i, "Bye")
print("Loop ended\n")

total = 100
while total > 0: 
    # get number from user
    print(total, " left")
    innum = int(input("Enter number : "))   
    if(innum<0):
      print("Can't use negative numbers")
      innum = 0
    total = total - innum
else:
    print ("total value became <= 0 i.e. ", total)
print("")

