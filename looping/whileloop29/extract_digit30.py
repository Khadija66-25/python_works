#print the last digit one by one like 
#ed num-12345
#5 4 3 2 1 line by line 

#loop number !=0
#       step1 extract last_digit = number%10
#       step2 floor number = number // 10


number = 274
while(number !=0):#274 !=0 27 !=0

    last_digit = number %10 #last digit = 27%10=4

    print(last_digit)# 4 7

    number = number //10 #number = 274//10=27