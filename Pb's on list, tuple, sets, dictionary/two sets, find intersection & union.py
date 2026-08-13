# Given two sets, find their intersection(common elements) and union(all unique elements combined).
# input: setA: {1,2,3,4,5} setB: {4,5,6,7,8}  output:Intersection: {4,5} Union: {1,2,3,4,5,6,7,8}

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

uset = set1.union(set2)
inset = set1.intersection(set2)

print(uset,inset)