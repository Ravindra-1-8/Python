# Find the minimum and maximum values in a list of numbers.
# Input: 15, 2, 7,25, 10
# Output: Mximum = 25, min = 2

l = [15,2,7,25,10]

# Hard Approach and important.
i = 0
max = l[0]
min = l[0]
for i in l:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"Maximum: {max}")
print(f"Minimum: {min}") 

# Easy Approach.
"""l.sort()
print(l[-1],l[0])"""