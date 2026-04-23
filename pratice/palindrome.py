#Check whether 1221 is a palindrome.




    #   or another method



s = input("enter: ")

lst = list(s)
lst.reverse()

if list(s) == lst:
    print("Palindrome")
else:
    print("Not Palindrome")