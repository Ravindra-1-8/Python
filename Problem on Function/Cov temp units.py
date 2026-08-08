def convunits(a):
    con1 = a * (9/5) + 32
    con2 = 273 + a
    con3 = (a - 32) * 5/9
    print(f"Temp in Fahrenheit:{con1}")
    print(f"Tem in Celsius:{con2}")
    print(f"Tem in Kelvin:{con3}")
x = int(input("Give value of a: "))
convunits(x)