#BMI Calculation

#read height
#read weight 

#BMI = weight_in_kg\height_in_meter**2

weight_in_kg = int(input("enter the weight in kg"))

height_in_cm = int(input("enter the height in cm"))

height_in_m = height_in_cm / 100

BMI = weight_in_kg / height_in_m**2

print("person with height",height_in_m,"and weight",weight_in_kg,"BMI = ",BMI)