# Find sum of all elements in a given list of numbers.
# input: [10, 20, 30, 40, 50]  Output: Sum of elements = 150

s = [10,20,30,40,50]

"""
sum = 0
length = len(s)

 # for loops method.
for i in range(0,length):
    sum += s[i]
print(sum)


# Method 1
for i in s:
    sum += i

print(sum)"""

# Using while loop.

sum = 0
i = 0

length = len(s)
while i < length:
    sum += s[i]
    i += 1
print(sum)