# append()
'''
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']

# clear()
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits) # Output: []

# extend()
fruits = ['apple', 'banana', 'cherry']
more_fruits = ['orange', 'grape']
fruits.extend(more_fruits)
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange

# index()
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana')) # Output: 1


fruits = ['apple', 'banana', 'cherry']
# insert()
fruits.insert(0, 'orange')
print(fruits) # Output: ['orange', 'apple', 'banana', 'cherry']

# count()
fruits = ['apple', 'banana', 'cherry', 'apple']
print(fruits.count('apple')) # Output: 2

# remove()
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits) # Output: ['apple', 'cherry']

# pop()
fruits = ['apple', 'banana', 'cherry']
fruits.pop()
print(fruits) # Output: ['apple', 'cherry']
'''

#reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse();
print(fruits) # Output: ['cherry', 'banana', 'apple']

# sort()
fruits = ['banana', 'cherry', 'apple']
fruits.sort();  
print(fruits) # Output: ['apple', 'banana', 'cherry']
numbers = [1,1,3,4,3,2,5,9,8,7,6]
numbers.sort()
print(numbers) # Output: [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
numbers.sort(reverse=True)
print(numbers) # Output: [9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]