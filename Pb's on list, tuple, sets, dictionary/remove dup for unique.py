# Remove duplicate elements from a list to create a new list with unique element.
# Input: [10,20,30,20,40,10,50]  Output: [10,20,30,40,50]

inp = input().split(',')


# List Method.

l = [int(item) for item in inp]

# remove duplicates and create unique items.

newL = []

# iterate over all the items.

for i in l:
    if i in newL:
        continue
    else:
        newL.append(i)

print(newL)


# Second Approach using Set
r = [int(a) for a in inp]

s = set(r)

newl = list(s)

print(newl)