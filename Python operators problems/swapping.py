#Problem 4: Swap the values of two variables without using a temporary variable.
#input: a = 10, b = 20.  output: After Swapping a = 20, b = 10

a = int(input("Give a: "))
b = int(input("Give b: "))

a += b
b = a - b
a = a - b
print(f"Value of a is: {a}")
print(f"Value of b is: {b}") 