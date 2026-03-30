#data types

# int,float,string,bool

number = 123 

print(type(number)) #it shows what kind of value is stored in the variable - type is function

name = "khadija"
 
print(type(name))

yoyo = True

print(type(yoyo))

rateing = 0.7
print(type(rateing))

#read total amount
#read the no of dines
#read th tip amount
#cal the individual splits

bill_amount = int(input("enter the bill amount"))

dines = int(input("enter the no of dines"))

tip_amount = int(input("enter tip tip_amount"))

total_bill = bill_amount+tip_amount

in_split = total_bill/dines
print(in_split)
