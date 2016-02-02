import itertools

def make_num(x):
    out = ""
    for y in x:
        out += y

    return int(out)


for x in range(500000):
    sort = sorted(str(x))
    if sort == sorted(str(x * 2)) and sort == sorted(str(x * 3)) and sort == sorted(str(x * 4)) and sort == sorted(str(x * 5)) and sort == sorted(str(x * 6)):
        print x