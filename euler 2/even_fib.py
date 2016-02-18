total = 0

l = [0, 1]

i = 2
while l[i-1] < 4000000:
    l.append(l[i-1] + l[i-2])

    if not l[i] % 2:
        total += l[i]

    i += 1;

print total