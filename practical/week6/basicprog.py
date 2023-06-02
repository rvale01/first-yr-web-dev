while True:
	want = input("What do you want for Xmas: (small letters): ")

	if want in ('book', 'phone', 'notebook', 'chocolate', 'pet', 'toy'):
   		print ("The ", want, " is yours")
   		choice = input("do you want something else: 'Y' or 'N':")
   		if choice in ['N', 'n']:
   			break
	else:
   		print ("I don't have ", want)
		   
print ("End of program")
