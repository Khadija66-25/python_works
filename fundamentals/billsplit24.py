#rbill_amount -read the bill amount

#dines_count -read the dines count

#cal tip as 12% of the bill amount

#add 8% of gst along with the bill amount

#cal the total amount and individaul split

bill_amount = int(input("enter the bill amount :"))

dines_count = int(input("enter the dines count :"))

tip_amount = (12/100)*bill_amount

gst_Amount = (8/100)*bill_amount

total_amount = bill_amount+ tip_amount+ gst_Amount

individual_Split = total_amount/dines_count

print(total_amount,"total_amount")

print(individual_Split,"individual split")