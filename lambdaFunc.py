'''
multi = lambda x, y: (x * 2, x + y)
multi_add = lambda x, y: x + y
print(multi_add(5, 3)) # Output: 8
print(multi(5, 3)) # Output: (10, 8)
'''

oddeven = lambda x: "Even" if x % 2 == 0 else "Odd"
print(oddeven(4)) # Output: Even