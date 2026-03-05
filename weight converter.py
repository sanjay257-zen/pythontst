#weight converter

weight = float(input("Enter the weight: "))
unit = input("Enter the unit (Kg/Lb): ").lower()

if unit == "kg":
    weight_in_pounds = weight * 2.20462
    print(f"The weight in pounds is: {weight_in_pounds:.2f}")
elif unit == "lb":
    weight_in_kilograms = weight * 0.453592
    print(f"The weight in kilograms is: {weight_in_kilograms:.2f}")
else:
    print(f"{unit} is an invalid unit. Please enter either 'kg' or 'lb'.")