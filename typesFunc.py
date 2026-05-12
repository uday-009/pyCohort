# Python Functions types

######## Functions are reusable blocks of code that perform a specific task. They can be categorized into two main types:
# 1. built in functions

# these are methods that are built into Python and can be used without needing to define them first.

print(len("Hello, World!")) # Output: 13
print(type(42)) # Output: <class 'int'>
print(max(1, 5, 3)) # Output: 5



# 2. user defined functions

def hello():
    print("Hello, World!")
    hello() # Output: Hello, World!