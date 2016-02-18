import math
import fractions



# num to be factored
n = 600851475143

def g(x):
    return (x**2 + 1) % n

def rho(x, y):
    d = 1

    while d == 1:
        x = g(x)
        y = g(g(y))
        a = math.fabs(x - y)
        d = fractions.gcd(a, n)
    if d == n: 
        return 0
    else:
        return d

factors = []

for x in range(10):
    for y in range(10):
        factors.append(rho(x, y))

print max(factors)