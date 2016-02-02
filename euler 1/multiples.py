def remainder(x):
    y = x / 3
    z = x / 5
    if not (type(y) and type(z)):
        print (x)
    elif y.is_integer() or z.is_integer():
        return x
    else:
        return 0

def sum_rem(x):
    total = 0
    for y in x:
        total += y

    return total

print (sum_rem([remainder(x) for x in range(1, 100)]))
