
food_items = [
    ["tea", "veg", 12],
    ["coffe", "veg", 20],
    ["dosa", "veg", 60],
    ["gheeroast", "veg", 80],
    ["masalaraost", "veg", 120],
    ["eggfriedrice", "non-veg", 160],
    ["vegfriedrice", "veg", 120]
]
#print the tiltle of the food

all_food = [it[0] for it in food_items ]

print(all_food)

#print the veg food only

veg_food = [it[0] for it in food_items if it[1]=="veg"]

print(veg_food)

#print the food under 100rs

low_food = [it[0] for it in food_items if it[2]<=100]

print(low_food)