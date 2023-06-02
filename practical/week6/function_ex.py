def min_max(x):     #defining function
    size = len(x)
    print (size)    #prints lenght of the list
    print (x)       #prints received list
    min1 = x[0]     #minimum value assumed
    max1 = x[0]     #maximum value assumed

    for num in range(0,size):   #for all list elements
        if min1 > x[num]:       
            min1 = x[num]
        if max1 < x[num]:
            max1 = x[num]

    return (min1, max1)         #returning list
                                #function definition ends
listnum = [12, 45, 22, 2, 0, 3, -5]    #main program - list
(minimum, maximum) = min_max(listnum)   #calling min_max function
print ("Smallest number is: " + str(minimum))   #printing outputs
print ("Largest number is: " + str(maximum))

