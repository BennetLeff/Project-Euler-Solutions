big = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        if str(x * y) == str(x * y)[::-1]:
            if (big < x*y):
                big = x*y


print big