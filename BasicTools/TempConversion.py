# Basic py code for temperature conversion
    #character code for degree is U+00B0

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {temp}\u00b0 F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is {temp}\u00b0 C")
else:
    print(f"{unit} is an invalid unit of measurement.")
