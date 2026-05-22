file_path = "C:\\Users\\Shahbas\\Desktop\\RESTART\\python\\Fileoperation\\emploo.csv"

fr = open(file_path,"r")

all_empolyees = []

for line in fr:
   
   #removing the \n from the right side of the  line
   
   line = line.rstrip("\n")

   #split line in to the data

   data = line.split(",")

   

   dictionary = {"id":data[0],"name":data[1],"dpt":data[2],"salary":data[3],"mail":data[4],"location":data[5]}
#append dict to empolye list
   all_empolyees.append(dictionary)



print(all_empolyees)
#print name those are in ekm
ekm_emplo = [e.get("name") for e in all_empolyees if e.get("location") == "ekm"]

#print ekm_e#print the highest salary emp

max_salary = max(all_empolyees,key=lambda e:e.get("salary"))
print(max_salary)