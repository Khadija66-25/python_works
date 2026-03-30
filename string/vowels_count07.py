#check whether the a is in apple

#text = "apple"

#if "a" in text:

   # print("yes")

#else:
    #print("no")


#VOWELS
#set text
#set vowels
#set v_count
#extract each character from text
#check character in vowels
#          increment v_count with one 

text = "wertyuiosdfghjklzxcvbnmasdfghjklwertyuiopcfgbA".casefold()

vowels = "aeiou"

v_Count = 0

for ch in text:

    if ch in vowels:

        v_Count+=1

print(f"vowels count = {v_Count}")

