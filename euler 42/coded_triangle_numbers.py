file = open("words.txt")

# just generate first 50, should be more than enough
# to check against
terms_triangle = [0.5 * x * (x+1) for x in range(0, 50)]
words = [x.split(",") for x in file][0]

# takes a word and prints sum of its ascii values 
# in 0-26 values
def word_val(x):
    total = 0
    word = x.strip("\"")
    for c in word:
        # subtract 64 from each character to map to 1-26
        total += ord(c) - 64

    return total

tri_word_total = 0

for word in words:
    if word_val(word) in terms_triangle:
        tri_word_total += 1

print tri_word_total