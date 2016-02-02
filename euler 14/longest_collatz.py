# store num and iterations of largest
max_collatz = {"num": 0, "iter": 0}

def collatz(x):
    num = x
    count = 0
    while not num == 1:
        if num % 2 == 0:
            num = num / 2.0
        else:
            num = (3 * num) + 1

        count += 1

    if count > max_collatz["iter"]:
        max_collatz["num"] = x
        max_collatz["iter"] = count

for x in range(1, 1000000):
    collatz(x)

print max_collatz