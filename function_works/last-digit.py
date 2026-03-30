#create a lasr_Digit_max of parametres of num1 and num2
#function should return if the last digit of num is greaterthan num2 else return num2


def last_digit(num1,num2):

    if num1%10 >=num2%10:

        return num1
    else:
        return num2
    

print(last_digit(345,126))