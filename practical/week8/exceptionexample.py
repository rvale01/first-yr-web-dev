x = int(input('Enter Dividend: '))
y = int(input('Enter Divisor: '))
try:
    z = x / y    
except ZeroDivisionError:
    print('Divisor should not be zero')
else:
    print('Result is ', z)
finally:
    print('Finally clause - end of program')
    


