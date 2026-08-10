# Count the no.of occurence of a specific element in a list.
# input: [1,2,3,2,1,4,2,5] 2 ouput: count of 2 = 3.

l = [int(cnt) for cnt in input().split(",")]

n = int(input())

count = 0

for i in l:
    if i == n:
        count += 1

print(f"count of 2 = {count}") 

# Easy Process
c = l.count(n)
print("Count of 2 =",c)