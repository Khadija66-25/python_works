#display the leap from 1879 to 2026

year = 1879

while(year<=2026):

    if  year%400==0 or (year % 4 == 0 and year % 100 != 0):

         print(year)

    year+=1


#A year is a leap year if:

#It is divisible by 4

#Except century years

#Unless the century year is divisible by 400