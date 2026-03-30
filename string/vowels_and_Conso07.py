#read the text ferom the user and display the vowels and consonant count


#set text
#set v_count as 0
#set c_count as 0
#extract  the each character from the text
        #chk character is vowel iif yes increment the v_count
        #else increment c_Count
#display v_count and c_count

text = "qwertasdfghjklrtghnm0oikjnhbasxcpa"

vowels = "aeiou"

v_count = 0

c_count = 0

for ch in text:

    if ch in vowels:

        v_count+=1

    else:
        c_count+=1

print(f'v_count ={v_count} c_count = {c_count}')
