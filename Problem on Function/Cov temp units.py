def convunits(x):
    if unit == "C":
        f = x * (9/5) + 32
        k = 273.15 + x

        print(f"Temp in Fahrenheit:{f}")
        print(f"Tem in Kelvin:{k}")

    elif unit == "F":
        c = (x - 32) * 5/9
        k = 273.15 + c 
        print(f"Tem in Celsius:{c}")
        print(f"Temp in Kelvin:{k}")

    elif unit == "K":
        c = (x - 32) * 5/9
        f = c * (9/5) + 32
        print(f"Temp in Celsius:{c}")
        print(f"Temp in Fahrenhiet:{f}")
    else:
        print("Invalid Unit.")


x = float(input("Enter Unit: "))
unit = input("Enter Units(C/F/K:)").upper()

convunits(x)