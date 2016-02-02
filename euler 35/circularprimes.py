from collections import deque

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(1000000)

def check_circ(n):
    perms = get_perms(n)

    count = 0
    for x in perms:
        if x in primes:
            count += 1
    
    if count == len(perms):
        return True
    else:
        return False

def get_perms(n):
    perms = []
    d = deque(str(n))
    
    compress = lambda nums: int(''.join(str(i) for i in nums))

    for x in range(0, len(str(n))):    
        d.rotate(1)
        perms += [compress(d)]

    return perms

circ_prime_list = []

check_prime_list = [x for x in primes if check_circ(x)]

print len(check_prime_list)