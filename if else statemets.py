#example 1
"""
w = input()

if w == "sunny":
    print("Cricket")
    print("Good to play")

elif w == "rainy":
    print("Rainy, Play Indoor games.")
    
else:
    print("Play with Robot doll.")
print("It's the final condition.")


#example 2
weather = "rainy"

if weather == "sunny":
    print("You can play with your car toy.")
else:
    print("It's not sunny, so you can play with a different toy.")

print("Enjoy your day!")
"""

#example 3
#input: "snowy","night","sunny","rainy".  output: "You can play with your car toy", "You can play with your boat toy","You can play with your snowman toy."
weather = "rainy"
time_of_day = "night"

if weather == "sunny":
    print("You can play with your car toy.")
elif weather == "rainy":
    print("You can play with your boat toy.") 
elif weather == "snowy" and time_of_day == "night":
    print("You can play with your teddy bear toy.")
else:
    print("You can play with your snowman toy.")

print("Stay warm and have a great time!")