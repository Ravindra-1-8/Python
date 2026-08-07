def greet_user(name, greetings="Hello"):
    return greetings + "! " + name + "."

greetings1 = greet_user("Bob")
greetings2 = greet_user("Charlie", "Hi")

print(greetings1)
print(greetings2)