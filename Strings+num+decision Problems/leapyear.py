"""Wap that takes a year as input and checks if it is a leap year or not.
Hint: A leap year is divisible by 4, excepts for years that are divisibel by 100 but not by 400.
Input: Enter a year: 2024
Output: It is a leap year.
"""

year = int(input())

leap = False

if year%100 == 0 and year%400 !=0:
    leap = False
elif year%4 == 0:
    leap = True
else:
    leap = False

print(leap)