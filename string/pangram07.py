#write the program to chck the given string in pangram

text = "the quick brown fox jumps over the lazy dog".lower()

alp = "abcdefghijklmnopqrstuvwxyz"

for ch in alp:
    if ch not in text:
        print("no")
        break
else:
    print("yes")