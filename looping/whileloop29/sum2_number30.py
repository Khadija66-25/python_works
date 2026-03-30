#find the  last digit of the number and sum of the number 
                                                         #LOGIC

# set number
# set sum
# loop
# extract last digit
# add last digit with sum
# remove last digit from number
# print sum


number = 567784326867

sum = 0

while(number!=0):

    last_digit = number % 10

    sum+=last_digit

    number = number//10

print(sum)



   

