def pythag_check(a, b, c):
    return (a**2 + b**2) == c**2

def thousand_check(a, b, c):
    return a + b + c == 1000

for a in range(1, 998):
    for b in range(1, 998):
        for c in range(1, 998):
            if a + b + c > 1000:
                break
            elif thousand_check(a, b, c):
                if pythag_check(a, b, c):
                    print a, b, c, a*b*c

