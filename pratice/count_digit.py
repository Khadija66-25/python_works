#Count digits in the number 987654.

num = 987654

count = 0

while(num!=0):

    last_digit = num%10

    count = count+last_digit

    count+=1

print(count)