product = {"code":56787,"tittle":"linen shirt","brand":"petergland","price":5678}


#add offer as 1000 iof offer is  not exist else update as current offer +500

if "offer" in product:

    product["offer"]+=500

else:

    product["offer"] =1000

print(product)