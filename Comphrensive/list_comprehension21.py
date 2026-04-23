#syntax

#  [expression iteration condition ]

#print a cubes new list of arr 

arr = [2,3,4,5]

cubes = [num**3 for num in arr]

print(arr)


                                                        #CONDITION CASES


even_numbers = [num for num in arr if num % 2 == 0]
print(even_numbers)

odd_numbers = [num for num in arr if num % 2 != 0]
print(odd_numbers)

num_gt_five = [num for num in arr if num > 5]
print(num_gt_five)


