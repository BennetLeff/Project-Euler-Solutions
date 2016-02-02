file = open("cipher.txt", "r")

text_list = [x.split(",") for x in file][0]

text = ""

count = 0

text = ""
for x in text_list:
    text += chr(int(x))

final_text = ""

def xor(num1, num2, num3):
    t = [num1, num2, num3]
    out = ""
    count = 0
    for x in text:
        out += chr(t[count] ^ ord(x))
        count = (count + 1) % 3
            

    return str(num1) + str(num2) + str(num3) + "\n" + out + "\n\n\n"

file = open("final.dat", "w+")

for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            file.write(xor(a, b, c))

file.close()    