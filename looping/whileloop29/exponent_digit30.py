#to find the number is armstrong number or not



#set num
#find digit_Count
# set sum as 0

# loop
    # extract digit
    # exponent
    # add exponent with sum
    # remove last digit
# dispaly sum


number = 1377


count = len(str(number))

sum = 0

while(number!=0):

    digit = number % 10

    exponent = digit ** count

    sum = sum + exponent

    number = number // 10

print(sum)