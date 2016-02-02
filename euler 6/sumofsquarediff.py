def sum_of_n(n):
    return sum(range(1, n+1))**2

def square_square_n(n):
    return sum([x**2 for x in range(1, n+1)])

print sum_of_n(100) - square_square_n(100)
