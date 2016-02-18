from fractions import gcd

def divide_all_20(x):
    for n in range(1, 20):
        if x % n == 0:
            pass
        else:
            return False
    return True

i = 35581710

while not divide_all_20(i):
    i += 10
    print i

print i