def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

n = 1000
length = len(get_primes(n))

while length < 10011:
    n += 10
    length = len(get_primes(n))
    print length, n

print get_primes(n)[10001-1]