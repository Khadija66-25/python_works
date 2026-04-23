# wanna count of the letter in this word

text = "goodmorning"

char_count = {}            # here me putting empty dict 

#to check one by one of the letter of the text , we are using for loops

for ch in text:               # ch is chuma term

    if ch in char_count:

        char_count[ch]+=1                     # here ,if it is there in empty box charcount should be incease by 1 

    else :

        char_count[ch] = 1              # if not charcount:key and 1 :value here


print(char_count)


             




