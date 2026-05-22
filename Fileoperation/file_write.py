#fw = open("C:\\\\Users\\\\Shahbas\\\\Desktop\\\\RESTART\\\\python\\\\Fileoperation\\\\greetings.txt","w")

# in this \\ has some issue fo that another method assign a path to variable 

#fw.write("good")
          #           LIKE THIS

file_path = "C:\\Users\\Shahbas\\Desktop\\RESTART\\python\\Fileoperation\\greetings.txt"

fw = open(file_path,"w")

#fw.write("Khadija the mass")


#no use u  can do i  the first method itself same issue here to 

#write from the list

greeting_list = ["good morning","good evng","good night"]

for g in greeting_list:

    fw.write(g+"\n")