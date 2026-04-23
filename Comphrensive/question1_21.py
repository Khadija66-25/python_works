#generate new list map num as num+1 if num>5 else num-1

arr = [ 2,3,4,6,7,8,10]
new_arr = [num+1 if num>5 else num-1 for num in arr]

print(new_arr)