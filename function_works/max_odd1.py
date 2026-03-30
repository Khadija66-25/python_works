def max_odd_num(number):

    while(number!=0):

        digit = number%10

        if digit %2!=0:

            print(number)

            break

        number = number//10


    max_odd_num(44768)




    #number = int(input("enter the num"))

#while(number!=0):

    #digit = number % 10

    #if number%2!=0:

        #print(number)

        #break

    #number = number //10