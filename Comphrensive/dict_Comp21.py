#print the dict comphen 

words = [ "apple","banana","carrot","drumstick","egg","fish"]

#from this i want the key as name of the frui a nd value as the char of the fruit 


word_dict = {w:len(w) for w in words}


print(word_dict)



arr = [6,7,8,9,10]

num_dict = {n:n**2 for n in arr} 

print(num_dict)

order = ["idly","tea","coffe","tea","idly","idly"]

new_order = {o:order.count(o) for o in order}

print(new_order)