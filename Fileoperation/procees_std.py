all_std_path = "C:\\Users\\Shahbas\\Desktop\\RESTART\\python\\Fileoperation\\all_std.txt"

passed_std_path = "C:\\Users\\Shahbas\\Desktop\\RESTART\\python\\Fileoperation\\passed_std.txt"

failed_std_path = "C:\\Users\\Shahbas\\Desktop\\RESTART\\python\\Fileoperation\\failed_std.txt"

f_all_std = open(all_std_path,"r")

f_failed_std = open(failed_std_path,"r")

f_passed_std = open(passed_std_path,"w")

all_std_set = set()

failed_std_set = set()

for name in f_all_std:

    all_std_set.add(name.rstrip("\n"))

print(all_std_set)

for name in f_failed_std:

    failed_std_set.add(name.rstrip("\n"))

print(failed_std_set)


passed_std_set = all_std_set.difference(failed_std_set)

print(passed_std_set)
#  => to wrie in file 

for name in passed_std_set:

    f_passed_std.write(name+"\n")

print(f_passed_std)




