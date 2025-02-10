# Basic python weight converter

weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds? (K or L): ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Weight in pounds: {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Weight in kilograms: {round(weight, 2)} {unit}")
else:
    print(f"{unit} was not valid.")