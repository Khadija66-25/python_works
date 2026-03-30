 


product_x = int(input("enter the product price:"))

profit_x = int(input("enter the profit % :"))

selling_price = product_x+ profit_x

percentage_x= profit_x/100* product_x

offer_price = selling_price-percentage_x

GST = 8

gst_Amount = (GST/100)*selling_price

total_cost = selling_price+gst_Amount

print(total_cost)