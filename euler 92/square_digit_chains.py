def get_square_digit(x):
    total = 0
    for dig in str(x):
        total += int(dig) ** 2
    return total

def find_num(x):
    count = 0
    num = get_square_digit(x)
    while not (num == 1) and not (num== 89):
        num = get_square_digit(num)
        count += 1

    if num == 1:
        return False
    if num == 89:
        return True

total = 0

for x in range(1, 10000000):
    if find_num(x):
        total += 1

print total