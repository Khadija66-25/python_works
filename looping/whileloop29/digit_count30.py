# set number
# set count as 0
# loop
    # extract last digit
    # increment count by 1
    # remove last digit
# display count


number= 465768

count = 0

while(number!=0):

    digit = number%10

    count+=1

    number = number //10

print(count)