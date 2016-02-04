def check_bounce(x):
    num         = str(x)
    digit       = int(num[0])
    moved_down  = False
    moved_up    = False
    for d in num:
        if int(d) > digit:
            moved_up = True
            digit = int(d)
        elif int(d) < digit:
            moved_down = True
            digit = int(d)

    return moved_down and moved_up



# found that the range is somewhere between 1587000
# and 1590000 through plugging in and checking guesses 
min_num = 1587095
max_num = 1590000

for y in range(min_num, max_num):    
    bouncies = []
    for x in range(100, y):
        if check_bounce(x):
            bouncies += [x]
    print float(len(bouncies)) / y
    if float(len(bouncies)) / y == 0.99:
        print y - 100 # subtract 100 because we start at 100 in range function
        break