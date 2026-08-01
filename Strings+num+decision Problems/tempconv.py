"""Build a temp converter pgm that allows user to convert temp b/w Celsius, kelvin, Fahrenhiet.
input: Enter temp: 32, Enter Units(K or F or C)
output: Temp in Fahrenheit: 89.6F, Temp in Kelvin: 305K. """
    
"""con1 = a * (9/5) + 32 
con2 = 273.15 + a
con3 = (a-32) * 5/9"""

a = int(input("Enter unit:"))
unit = input("Enter units(C/F/K):").upper()

if unit == "C":
    f = a * (9/5) + 32
    k = a + 273.15
    print(f"Fahrenheit: {f}")
    print(f"Kelvin: {k}")

elif unit == "F":
    c = (a - 32)* 5/9
    k = a + 273.15
    print(f"Celius: {c}")
    print(f"Kelvin: {k}")

elif unit == "K":
    f = a * (9/5) + 32
    c = (a - 32) * 5/9
    print(f"Fahrenheit: {f}")
    print(f"Celsius: {c}")

else:
    print("Invalid Unit.") 