n = int(input("Give value of N: "))

fact = 1
while n > 0:
    fact = fact * n
    n -= 1      #(n,n-1,n-2,......1)
print(fact)