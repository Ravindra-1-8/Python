#Exercise on String slicing.
#problem 1
# Print the first 5 characters of a string.
"""P1 ="PythonProgramming"
print(P1[0:5])"""
#output: Pytho

# Problem 2
#Print the last 4 characters of a string.
"""print(P1[13:17])"""
#output: "ming"

#Problem 3
#Print every second character.
"""print(P1[::2])"""
#output: "PtoPormig"

#Problem 4: Reverse a string using slicing.
"""P1 = "Python"
print(P1[::-1])"""
# output: "nohtyP"

#Intermediate Problems
#Problem 1: Print string except first and last character
"""I = "Programming"
print(I[1:10]) #print(I[1:-1])"""

#Problem 2: Print first half of a string.
C = "Computer"
"""print(C[:4])"""
# output: "Comp"

#Problem 3: Print second half of the string.
"""print(C[4:])"""
#output: "uter"

#Problem 4: Print every third character.
"""E = "abcdefghijklmnopqrstyvwxyz"
print(E[::3])"""
#Output: "adgjmpsvy"

#Problem 5: Reverse only first 5 characters.
"""R = "PythonProgramming"
print(R[:5][::-1]+R[5:])"""