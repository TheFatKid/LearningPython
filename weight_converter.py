#Input the weight as a number
#Get if the number is in pounds or in kg
#If it is in pounds, pounds=kilograms×2.20462
#Else, if it is in kgs, multiply with 0.45359237
#convert_to_pounds = weight*0.45359237
#convert_to_kgs = weight*2.20462

weight = int(input("Weight :"))
pounds_or_kg = input("(L)bs or (K)g :")

if pounds_or_kg.upper() == "L":
    converted = weight*0.45
    print(f"You are {converted} kgs.")
elif pounds_or_kg.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds.")
else:
    print("Error: Input must be either 'K' or 'L'.")


