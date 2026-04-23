bikes = [
    ["passion-pro", "hero", 89000, "petrol", 125],
    ["passion-plus", "hero", 89000, "petrol", 125],
    ["activa", "honda", 120000, "petrol", 125],
    ["xpulse", "hero", 139000, "petrol", 150],
    ["hunter", "re", 200000, "petrol", 350],
    ["meteor", "re", 230000, "petrol", 350],
    ["triumph-speed-400x", "triumph", 350000, "petrol", 400],
    ["s1-pro", "ola", 140000, "ev", 120],
    ["ather450x", "ather", 160000, "ev", 150]
]

all_bike_names = [b[0] for b in bikes]
print(all_bike_names)

all_bike_prices = [b[2] for b in bikes]
print(all_bike_prices)

fuel_varients = {b[3] for b in bikes} #y set is used means=>so ut wont allowed duplicates
print(fuel_varients)

#print "ev" bikes only
ev_bikes = [b[0] for b in bikes if b[3]=="ev"]
print(ev_bikes)

#print the costly bike '
def get_price(lst):

    return lst[2]

cost = max(bikes,key=get_price)
print(cost)
