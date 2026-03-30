# print whether is prime number or not?

# read number

# set is_prime as True

# loop
    # chk i is divisor of number
    #


number = int(input("enter number"))

is_prime = True

for i in range(2,number):

    if number % i ==0:

        is_prime = False

        break

print(f"prime number" if is_prime ==True else "not prime number")