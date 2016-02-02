from math import log10

file = open("base_exp.txt")

nums = []

for x in file:
    base = int(x.split(",")[0])
    expo = int(x.split(",")[1])
    nums += [(base, expo, expo * log10(base))]

def find_max(x):
    max_num = 0
    for y in x:
        if y[2] > max_num:
            max_num = y[2]

    return max_num

max_log = find_max(nums)

count = 1
for z in nums:
    if z[2] == max_log:
        print z, count
    count += 1

