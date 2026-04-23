lst = [1, 2, 3, 5]
#      0   1  2  3         =>index
#      i   j                =>logic to find thr diff
#      1   2   3  4        =>wile using length -it will calculate like this 



for i in range (0,len(lst)-1):                 #nammek length 3 vara pognda ,2 vara mathi so that we are using "len(lst)-1"

    j = i+1

    difference = lst[j] - lst[i]


    if difference!=1:

       print(lst[i]+1 , "is a missing number")

       break

   

