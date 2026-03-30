#create a  list expense [10000,120000,130000,140000]
#update 12000 as 12500
#display all expenses
#display total expenses
#display highest expense
#display avg expense


# +ve        0      1     2     3
expenses = [10000,12000,13000,14000]
# -ve        -4    -3     -2   -1

print(expenses)

expenses[1] = 12500

print(expenses)

#iteration
#indexing

for i in range(0,len(expenses)):      #=>len expenses-untill where the expenses is ending

    print(expenses[i])


#for e in expenses:

   # print(e)

   #total expense 

#>method 1
total_exp = 0
for i in range(0,len(expenses)):

    total_exp += expenses[i]

print(total_exp)

#> method 2

for e in range(0,len(expenses)):

    total_exp +=e

    print(total_exp)

    #highest expenses 

high = max(expenses)

print(high)