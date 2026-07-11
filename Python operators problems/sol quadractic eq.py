#Problem 3: Solving quadratic Equations
#input: a =1, b=-3, c=2  output: Roots:(2.0,1.0)  (topic:I/o, variable, Arithmetic Operators.)

a = int(input("Give a: "))
b = int(input("Give b: "))
c = int(input("Give c: "))

root1 = 0
root2 = (0)
d = (b**2) - 4 * a * c
root1 = (-b + (d ** (0.5)))/ 2 * a
root2 = (-b - (d ** (0.5)))/ 2 * a

print(f"(Root:{root1},{root2})")