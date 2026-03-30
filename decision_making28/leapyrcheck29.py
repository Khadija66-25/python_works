#check the year and century year is leap yr or not

year = int(input("enter year :"))

if year % 100 ==0 and year % 400 ==0 or year %100 !=0 and year %4 ==0:
    
    print(year,"is the leap year")

else:
    print(year,"is not the leap year")