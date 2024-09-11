import math
num1=input("Enter the original number and unit you want to change(use space in the middle)")
number, unit = num1.split()
    number = float(number)
    # Initialize a variable to store the conversion result and the converted unit
    converted_value = 0
    converted_unit = ""































number, unit = num1.split()
 if unit == "cm":
        converted_value = number / 2.54  # Convert cm to inches
        converted_unit = "in"
    elif unit == "in":
        converted_value = number * 2.54  # Convert inches to cm
        converted_unit = "cm"
    elif unit == "yd":
        converted_value = number * 0.9144  # Convert yards to meters
        converted_unit = "m"
    elif unit == "m":
        converted_value = number / 0.9144  # Convert meters to yards
        converted_unit = "yd"
    elif unit == "oz":
        converted_value = number* 28.349523125  # Convert ounces to grams
        converted_unit = "g"
    elif unit == "g":
        converted_value = number / 28.349523125  # Convert grams to ounces
        converted_unit = "oz"
    elif unit == "lb":
        converted_value = number * 0.45359237  # Convert pounds to kilograms
        converted_unit = "kg"
    elif unit == "kg":
        converted_value = number / 0.45359237  # Convert kilograms to pounds
        converted_unit = "lb"
    else:
        print("Invalid unit entered. Please use a valid unit like 'cm', 'in', 'yd', 'm', 'oz', 'g', 'lb', or 'kg'.")
        return

