#Problem 5: Converting Temperature Units
#input: temperature_celsius = 30.  output: Temperature in fahrenheit: 86.0, Temperature in kelvin: 303.15

a = int(input("Give a: "))

con1 = a * (9/5) + 32
con2 = 273 + a
print(f"Temperarure in Fahrenheit: {con1}")
print(f"Temperature in Kelvin: {con2}")