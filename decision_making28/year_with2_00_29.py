#read a year
#display a century yr if ending with two zeros
#else display non century yr

year = int(input("enter year: "))

if year%100 ==0:
    print("century year")

else:
    print("non century year")