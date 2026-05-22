words = ["hello","madam","racecar","pangram","hai"]

file_path ="C:\\Users\\Shahbas\\Desktop\\RESTART\\python\\Fileoperation\\word.txt"
            
fa = open(file_path,"w")

for arr in words:

    if arr ==arr[::-1]:

        fa.write(arr+"\n")

    




     








