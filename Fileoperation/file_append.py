#we have to some elements to the greetings file

food_items = ["idly","pongal","dosa"]

fw = open("C:\\Users\\Shahbas\Desktop\RESTART\python\Fileoperation\greetings.txt","a") #=> " a" - is append 

                                    
for item in food_items:

    fw.write(item+"\n")
                                           


