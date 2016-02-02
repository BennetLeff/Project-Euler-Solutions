from math import factorial

total = 0
x = str(factorial(100))

for y in x:
    total += int(y)

print total
