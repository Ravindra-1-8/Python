my_set = {1,1,2,3,4,5,6,7}

set1 = my_set.copy()   #Copy every elements in the set.
set2 = my_set.pop()    # pops the first element in the set.

my_set.update([9])   # updates the element in the beginning of the set
set3 = my_set

print(set1) 
print(set2)
print(f"Updated set:{set3}")

set4 = my_set.clear()
print("cleared set:",set4)