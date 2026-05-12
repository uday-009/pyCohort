'''

my_set = {1,2, 5,6,3,4}
print(my_set)

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set) # Output: {1, 2, 4, 5}

my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set) # Output: {1, 2, 4, 5}

my_set = {1, 2, 3, 4, 5}
my_set.intersection_update({3, 4, 5, 6})
print(my_set) # Output: {3, 4, 5}
'''
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b)) # Output: {1, 2, 3, 4, 5}
print(a.intersection(b)) # Output: {3}
print(a|b) # Output: {1, 2, 3, 4, 5}
print(a&b) # Output: {3}    