#Read a number and print the sum of its digits 697098089

num = 697098089

sum = 0

while (num!=0):

    last = num%10

    sum = sum +last

    num = num // 10

print(sum)
