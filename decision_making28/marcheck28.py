#read 3 marks out of 50 per each subject

#calculate the total

#base on total display

#total >140 #good

#130-140 #avg

#<130 #poor

mark1 = int(input("enter the mark1:"))

mark2 = int(input("enter the mark2:"))

mark3 = int(input("enter the mark3:"))

total = mark1 + mark2 + mark3

print(total)

if total>140:
    print("good")
elif total<130 and total<=140:
    print("avg")
else:
    print("poor")

