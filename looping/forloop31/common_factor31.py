num1 = int(input("enter num1"))  # 4

num2 = int(input("enter number2"))  # 16

limit = min(num1, num2)

for i in range(1, limit + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
