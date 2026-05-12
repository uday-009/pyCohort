
def hello():
    global x
    x = "Hello, World!"
    print(x)

hello() # Output: Hello, World!
print(x) # This will raise a NameError because x is not defined in the global scope