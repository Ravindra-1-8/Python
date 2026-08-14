import sys
sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

i = 0
def greet():
    global i
    i += 1
    print(f"Hello {i}")
    greet()

greet() # calling the function greet().9