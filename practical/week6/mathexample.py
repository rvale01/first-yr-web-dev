from math import * 

n = input("enter a number")
n = int(n)+1
for a in range(1,n):
	n_sqr = a * a
	n_sqrt = sqrt(a)
	n_cube = pow(a, 3)
	print ("number is ", a, " square is ", n_sqr, " square root is ", n_sqrt, " cube is ", n_cube)
print ("end of program")


str = ""
n = input("enter a number ")

n = int(n)+1
for a in range(1,n):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a, b, c)
print ("end of program")

n = input("enter a number")

n = int(n)+1
for a in range(1,n):
	n_sqr = a * a
	n_sqrt = int(sqrt(a))
	print ("number is " + a + " squrare is " + n_sqr + " n_sqrt is " + n_sqrt)
print ("end of program")

