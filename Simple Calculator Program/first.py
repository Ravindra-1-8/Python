""" 1. create a basic claculator program that performs (+,-/,*).
 Ask user to enter two numbers & choose an operation.
 Display result accordingly.
 Handle potential errors gracefully.   
 
 Input: num1
        num2
        operation(+,-,*,/)
 """

num1 = int(input("Give 1st number: "))
num2 = int(input("Give 2nd number: "))
operator = input("Give operator: ")

if operator == "+":
    print(f"Addition of two numbers is {num1+num2}")
elif operator == "-":
    print(f"Substraction of two numbers is {num1-num2}")
elif operator == "*":
    print(f"Multiplication of two numbers is {num1*num2}")
elif operator == "/":
    print(f"Division of two numbers is {num1/num2}")

else:
    print("Invalid Operator.")