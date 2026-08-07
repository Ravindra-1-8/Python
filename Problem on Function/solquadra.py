def calculateRoots(x,y,z):
    root1 = 0
    root2 = 0
    d = (y**2) - 4 * x * z
    root1 = (-y + (d**(0.5)))/2*x
    root2 = (-y - (d**(0.5)))/2*x
    print(f"Roots:({root1},{root2})")

a = int(input("Give x value: "))
b = int(input("Give y value: "))
c = int(input("Give z value: "))

calculateRoots(a,b,c)