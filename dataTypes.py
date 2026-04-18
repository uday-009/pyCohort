# int
c = 30.5;
#float
a = 10.5;
#complex
b = 1+ 2j; 
# dictionary
d = {"key1": "value1", "key2": "value2"};

print(type(b), type(a), type(d))

#list
my_list = [1,2,3,10];

print(my_list[0]) # Accessing the first element of the list
print(my_list[0:4]) # Accessing a slice of the list

my_list2 = ["apple","grapes","banana"]; # list is mutable
my_list_tuple = ("apple","grapes","banana"); # tuple is immutable
my_list2.append("orange") # Adding an element to the list
my_list2.insert(0, "mango") # Inserting an element at a specific index
print(my_list2) 

# Create a dynamic class named 'MyClass' that inherits from 'object' and has an attribute 'x'
MyClass = type('MyClass', (object,), {'x': 5})

obj = MyClass()
print(obj.x) 

g = 10;
h = '20';
i = int(h); # Type casting from string to integer
print(g + i) # Output: 30
