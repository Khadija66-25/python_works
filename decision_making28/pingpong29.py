#if the number is divisible by 3 PING,
# print ping,if it is 5 by 5 print pong,
#  if it is % by 15 print  PINGPONG


number = int(input("enter the number: "))

if number % 15==0:
    print("PING")

elif number% 5==0:
    print("PONG")

elif number% 3==0:
    print("PINGPONG")

else:
    print("invalid")