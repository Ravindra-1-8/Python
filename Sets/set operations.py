set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10,5}

fset1 = set1.union(set2)
fset2 = set1.intersection(set2)

print(fset1)
print(fset2) 

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,18}

res = s2.difference(s1)
print(res)

r1 = {1,3,5,7}
r2 = {1,2,3,4,5,6,7}
res2 = r1.symmetric_difference(r2)
print(res2)

f2 = {2,4,5,2,5,7}
f1 = {1,1,3,4,5,6}
union = f1.union(f2)
intersection = f1.intersection(f2) # return the common elements in both the sets.
print(union)
print(intersection)