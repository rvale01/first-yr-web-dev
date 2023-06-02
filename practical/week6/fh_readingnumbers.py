fh = open('numbers.txt')

num_list = []
for num in fh:
	#print('Number is ', num) #will print with newline   
	print('Number is with rstrip ', num.rstrip())    
	num_list.append(int(num))

fh.close()

print ('List is: ', num_list)
num_list.sort()
print ('Sorted list is: ', num_list)

large_num = max(num_list)
small_num = min(num_list)
total_num = sum(num_list)

print ('Largest number: ', large_num)
print ('Smallest number: ', small_num)
print ('Sum is: ', total_num)







