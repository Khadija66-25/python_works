from random import randint

target = randint(1, 10)

while True:
    number = int(input("guess the number "))

    if number == target:
        print("congrats")
        break
