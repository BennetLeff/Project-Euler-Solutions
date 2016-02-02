out = []
def dec_to_bin(x):
    return int(bin(x)[2:])

for x in range(1, 1000001):
    if str(x)[::-1] == str(x) and str(dec_to_bin(x)) == str(dec_to_bin(x))[::-1]:
        print str(x), dec_to_bin(x)
        out += [x] 

print sum(out)