def arithmetic_sum(first, *more):
    return (first + sum(more))

def tempChange(a):
    fah = (a * 9)/5 + 32
    return fah

print (arithmetic_sum(1,2))
print (arithmetic_sum(1,2,3))
print (arithmetic_sum(1,2,3,4))
print (arithmetic_sum(1,2,3,4,5))
print (arithmetic_sum(1,2,3,4,5,6))

print(tempChange(30))
