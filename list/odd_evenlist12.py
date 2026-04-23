

arr = [1, 10, 11, 12, 34, 35]

even = []
odd = []

for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if even:
    print("Even numbers:", even)
else:
    print("Odd numbers:", odd)