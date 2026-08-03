#Take a pos integer N as input and calculate the sum of fist N natural numbers.

n = int(input("Give n value: "))

i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)