"""
wap that takes a string input form the user and checks if it is a plaindrome or not.
A palindrome is a word, phrase, number or sequence of characters that reads the same backward as forward.
Input: "radar"
Output: It is a palindrome.
"""

#Palindrome:the word will be same when read it in forward & backward.
s = input("Give a string: ")

reverse = s[::-1]

if reverse == s:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")