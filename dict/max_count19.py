#continue of text_count

text = "goodmorning"

char_count = {}            # here me putting empty dict 

#to check one by one of the letter of the text , we are using for loops

for ch in text:               # ch is chuma term

    if ch in char_count:

        char_count[ch]+=1                     # here ,if it is there in empty box charcount should be incease by 1 

    else :

        char_count[ch] = 1              # if not charcount:key and 1 :value here


print(char_count)           #{'g': 2, 'o': 3, 'd': 1, 'm': 1, 'r': 1, 'n': 2, 'i': 1}              
                            # FROM THIS PRINT THE MAX COUNT OF THIS


max_freq = 0

max_freq_dict = {}

for k,v in char_count.items():           # k-key v-value

    if v > max_freq:

        max_freq = v

        max_freq_dict.clear()

        max_freq_dict[k]=v

print(max_freq_dict)





