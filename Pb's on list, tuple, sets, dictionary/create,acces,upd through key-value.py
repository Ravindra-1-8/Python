# Create dictionaries, access values, update values, and iterate through key-value pairs.
# input: my_dict = {name: 'john','age':30,'city':'new york'}  output: {name: John, age: 31, city: SanFrancisco.}


# Predefined input.
"""my_dict = {'name': 'John',
           'age': 31,
           'city':'New York'
           }
# Iterating using key-vaue pairs
for i,j in my_dict.items():
    print(i,j)"""


my_dict = {}
a = input("Give name: ")
age = int(input("Give age: "))
c = input("City: ")

my_dict["name"] = a
my_dict["age"] = age
my_dict["city"] = c

my_dict["age"] = 66 # updating the values.
print(my_dict)