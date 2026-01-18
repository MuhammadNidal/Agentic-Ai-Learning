dictionary={
    "name": "John",
    "age": 30,
    "city": "Peshawar",
    "hobbies": ["reading", "gaming", "coding"],
}
print(dictionary)
print(dictionary["age"])
print(dictionary["name"])
print(dictionary.get("city"))
print(dictionary.get("country"))  # Default value if key not found
dictionary["country"] = "Pakistan"  # Adding a new key-value pair
print(dictionary)
dictionary["age"]=90
print(dictionary)

# methods
dictionary.pop("city")  # Removes the key "city"
print(dictionary)

dictionary.popitem()  # Removes the last inserted key-value pair
print(dictionary)
dictionary.popitem()  # Removes the last inserted key-value pair again
print(dictionary)

del dictionary["name"]  # Deletes the key "name"
print(dictionary)



my_dict = {"name": "Nidal", "age": 23, "skills": ["Python", "React"]}
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'skills'])
print(my_dict.values())  # Output: dict_values(['Nidal', 23, ['Python', 'React']])
print(my_dict.items())  # Output: dict_items([('name', 'Nidal'), ('age', 23), ('skills', ['Python', 'React'])])


for key in my_dict:
    print(key)  # Iterating through keys
for key, value in my_dict.items():  
    print(key, value)  # Iterating through key-value pairs
for key in my_dict.values():
    print(key)  # Iterating through values


#     What is Dictionary Comprehension? 🤔

# Dictionary comprehension is a short and clean way to create a dictionary from:
# a list
# another dictionary
# any iterable (like range, tuple, etc.)
# Instead of writing many lines of code, you can do it in one line.
# Normal Way (Without Comprehension)

# {key: value for item in iterable}

squares = {}

for i in range(1, 6):
    squares[i] = i * i

print(squares)

# Output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squares = {i: i*i for i in range(1, 6)}
print(squares)


    