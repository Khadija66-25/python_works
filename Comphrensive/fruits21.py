arr = ["apple","guva","grape"]     # wanna print the  using normal method

cap_list = []

for item in arr:

    cap_list.append(item.upper())

print(cap_list)


#comprehension method

array = ["apple","guva","grape","mango"]

fruits = [item.upper() for item in array]

print(fruits)



