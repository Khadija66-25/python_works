file_path = "c:\\Users\\Shahbas\\Desktop\\RESTART\\python\\Fileoperation\\food_logs.csv"


fr = open(file_path,"r")

food_logs = []

for line in fr:

    data = line.rstrip("\n").split(",")

    if len(data)>1:

        dictionary = {
            "date":data[0],
            "meal_type":data[1],
            "name":data[2],
            "serving_Size":data[3],
            "calories":data[4]
            }

        food_logs.append(dictionary)

print(food_logs)

    