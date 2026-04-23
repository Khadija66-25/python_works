# text="this is a python program to find most recursive word this python program is simple "

# display most frequent word

text="this is a python program to find most recursive word this python program is simple "

words = text.split(" ")

word_count = {}

for w in words:

    if w in word_count:

        word_count[w]+=1

    else:
        word_count[w]=1

print(word_count)  #{'this': 2, 'is': 2, 'a': 1, 'python': 2, 'program': 2, 'to': 1, 'find': 1, 'most': 1, 'recursive': 1, 'word': 1, 'simple': 1, '': 1}

#max_word = ""

#max_count = 0

#for w in word_count:

 #   if word_count[w] > max_count:
  #      max_count = word_count[w]
   #     max_word = w

 
#print(max_word)
#print(max_count)

srt_word = sorted(word_count,key=word_count.get,reverse=True) # namma normal ah wordcount mattum kudutha ah , oru order la varth but
        #when we are putting  key and reverse crt value order la varum like 33 22 11 

print(srt_word)




