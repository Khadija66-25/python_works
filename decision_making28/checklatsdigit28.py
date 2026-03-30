#read the program
#write a prgm that display the last digit of num that odd or even

num = int(input("enter the number :"))

last_digit = num%10

if last_digit%2==0:
    print("it is even number")
else:
    print("it is odd number")