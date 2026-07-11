"""
name = input()
print("My name is",name)

Stirng input:

name = input("My name is: ")

print(name)

integer input: eg1
number = input("Give number: ")
number2 = int(number)
print(type(number2))

eg2
number = int(input("Hello: ")), float(input("Hello: "))
print(type(number))
 
eg3
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello, " +name+ "! Your are",age, " years old.")

Output:

t = (1, 2, 3, 4)
print(t)
print(*t)

a = int(input("Give a value: "))
b = int(input("Give b value: "))

print(a,b,a,b,sep= ", ", end = ".")  

#example 1
name = input("Enter your name: ")
print("Hello", name, sep=", ", end = "!")

#example 2
num = int(input("Give value of num: "))
print("You enterd:",num, sep=" ",end=".")

#example 3 float I/o
#Expected input: 3.14, Expected Output: "Value of Pi 3.14"
pi = float(input("pi: "))
print("Value of Pi: ",pi,sep="",end=".")


#example 4: Multiple inputs in single line(sum)
a = input()
x,y,z = a.split(" ")# for multiple input
sum = int(x)+int(y)+int(z)
print(sum)


#example 5: Specifying Separator in Output
#input: John, 25.   output: Name:John, Age: 25
a = input("Enter you Name and Age: ")
name,age = a.split(",")
print("Name:",name,",Age:",age, sep="")


#example 6: End Parameter in Output
#Input: 5, Output: "Countdown: 5 4 3 2 1 Blast Off!"
n = int(input("Enter n: "))# need to use loops here.
print("Countdown: 5 4 3 2 1 ", end="Blast Off!")


#example 7: Arithmatic Operators
#input: 10,5  output: "Addition:15, Substraction:5, Multiplication:50, Division:2.0"
x,y = input("Enter a & b values: ").split(",")#refer example5
a = int(x)
b = int(y)
print("Addition:",a+b,"Substracton:",a-b,"Multiplication:",a*b,"Division:",a/b) 



#example 11: Formatting Output using f-strings.
#input: "Alice",25  output: "Name: Alice,Age: 25 years"
x,y = input("Enter your name and age: ").split(",")

print(f"Name:{x},Age:{y}years")


#example 8: Comparison Operators
#input: 10,5  output:"10>5:true, 10<5: False, 10 == 5, 10 != 5: True"
#
x,y = (input("Enter values of a & b: ").split(","))
a = int(x)
b = int(y)
print(f"10 < 5: {a < b},10 > 5: {a > b}, 10 == 5 {a == b},10 != 5: {a != b}")


#example 9: Logical Operators
#input: True,False  output: "True or False:True,not True: False"

a = True
b = False
print("True or False:",a or b,sep="")
print("not True:",not a,sep="")
"""

#example 10: Taking yes/no input and handling case Sensitivity
#input: Yes(or yes, YES,YES,yEs, etc.) output: "You Entered: Yes"

x = ("Yes, yes, YES, yEs, etc.")
a = input("Enter yes/no: ")

print("You Entered: ",a)

