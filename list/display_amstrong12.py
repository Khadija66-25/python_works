#display the amstrong number


number = int(input("enter the num :"))


original =  number
digit_count = len(str(number))
sum = 0

# loop
while(number != 0):  # 153 → 15 != 0 → 1 != 0

    digit = number % 10   # 3, 5, 1

    exponent = digit ** digit_count   # 27, 125, 1

    sum += exponent   # 27 + 125 = 152 + 1 = 153

    number = number // 10   # 0

print("armstrong number" if original == sum else "not armstrong")