
# step1: set sum as 0
# step2: last_digit
# step3: add last digit with sum
# step4: floor

number = 174

sum = 0

while(number!=0):

    last_digit = number%10

    sum+=last_digit

    number = number//10

print(sum)

    
