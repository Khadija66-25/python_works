#create a new list of words starting with vowels

words = [ "apple","banana","carrot","drumstick","egg","fish"]

#filtering

new_words = [w for w in words if w[0].lower() in "aeiou"]

print(new_words)



#reduce

#print the longest word from the words

longest_word = max(words,key=len)    # here y bcoz key means python dont know that we are askinga abt the char len or word length

print(longest_word)
