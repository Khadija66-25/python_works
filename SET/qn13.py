all_std = ["fathima","khadija","sumaya","kindi","gana","amritha"]

failed_Std = ["irsha","thapsi","gana","sumaya"]

#hw many std attend the exam list of their names

set_all = set(all_std)
set_fail = set(failed_Std)

all_names = set_all.union(set_fail)

print("name of every std:",all_names)

failed = set_all.intersection(set_fail)

print(failed)



