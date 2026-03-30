#check whether the num is duvisible by 3,7,5

num = int(input("enter the num :"))

result = num %3 ==0 and num%5 ==0 and num%7==0
print(result)