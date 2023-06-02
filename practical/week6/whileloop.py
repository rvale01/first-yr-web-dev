n = int(input("Enter a number: "))

sum = 0
count = 1
while count <= n:
    sum = sum + count
    count += 1

print("Sum of 1 until ", n, " : ", sum)
