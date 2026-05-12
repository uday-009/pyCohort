my_dict = {
    "name": "uday",
    "age": 22,
    "city": "hyderabad"
}

print(my_dict) # Output: {'name': 'uday', 'age': 22, 'city': 'hyderabad'}
print(type(my_dict["name"])) # Output: <class 'str'>s

print(my_dict.get("age")) # Output: 22
print(my_dict.get("country", "not found")) # Output: 'not found'

print(my_dict.keys()) # Output: dict_keys(['name', 'age', 'city'])

a = my_dict.keys()
print(type(a)) # Output: <class 'dict_keys'>

print(my_dict.values()) # Output: dict_values(['uday', 22, 'hyderabad'])
b = my_dict.values()
print(type(b)) # Output: <class 'dict_values'>