#word_Count-wann chk the count

text = "hello hai hello hai hai hai"

#step1: split the text into word

words = text.split(" ")   #  =>("  ") it is space 

#step2 : create an empty dic

wc = {}

#step3: extract the each word from the words

for w in words:

    #add w as the key and value as 1 if w not exist else update w as of current value with 1


    if w in wc:

        wc[w]+=1

    else:

        wc[w]=1

print(wc)


