#print the panlndrome string from the list

arr = ["word","madam","racecar","car"]

for w in arr:

    if w == w[::-1]:
       print(w)


       #LIST COMPREHENSION METHOD



dad= [w for w in arr if w==w[::-1]]

print(dad)

#reverse that arr ?

reversed_arr = arr[::-1]    #=>this how u should dp

print(reversed_arr)



