# What Are Magic Methods in Python?

# Magic methods (also called dunder methods) are special methods in Python that:
# Start and end with double underscores (__method__)
# Are automatically called by Python
# Let you define how objects behave with built-in operations

# Examples:
# __init__      # object creation
# __str__       # string representation
# __add__       # + operator
# __len__       # len() function

# Why Are Magic Methods Used?
# Magic methods allow you to:
# Customize object behavior
# Make objects work with operators (+, -, ==)
# Integrate objects with built-in functions (len(), print())
# Write clean, readable, and Pythonic code

# Most Common Magic Methods (With Examples)
# 1️⃣ __init__ – Constructor

# Called when an object is created.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s = Student("Alice", 20)

# 2️⃣ __str__ – String Representation
# Controls what print(object) displays.
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Student name is {self.name}"

# print(Student("Bob"))

# Output:
# Student name is Bob

# 3️⃣ __repr__ – Official Representation

# Used for debugging (called by repr()).
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Student('{self.name}')"

# 4️⃣ __add__ – + Operator Overloading
# class Book:
#     def __init__(self, pages):
#         self.pages = pages

#     def __add__(self, other):
#         return self.pages + other.pages

# b1 = Book(100)
# b2 = Book(200)
# print(b1 + b2)
# Output:
# 300

# 5️⃣ __len__ – len() Function
# class Playlist:
#     def __init__(self, songs):
#         self.songs = songs

#     def __len__(self):
#         return len(self.songs)

# p = Playlist(["song1", "song2", "song3"])
# print(len(p))

# 6️⃣ __eq__ – Equality (==)
# class Person:
#     def __init__(self, age):
#         self.age = age

#     def __eq__(self, other):
#         return self.age == other.age

# p1 = Person(25)
# p2 = Person(25)

# print(p1 == p2)


# Output:

# True

# 7️⃣ __del__ – Destructor

# Called when an object is deleted.

# class Demo:
#     def __del__(self):
#         print("Object destroyed")

# d = Demo()
# del d


# ⚠️ Not commonly used due to garbage collection behavior.

# Common Magic Method Categories
# Category	Examples
# Object creation	__init__, __new__
# String display	__str__, __repr__
# Operators	__add__, __sub__, __mul__
# Comparison	__eq__, __lt__, __gt__
# Containers	__len__, __getitem__
# Context manager	__enter__, __exit__
# Simple Real-World Analogy

# Think of magic methods as remote-control buttons:

# Press + → Python calls __add__
# Use len() → Python calls __len__
# Print object → Python calls __str__
# You don’t call them directly — Python does it for you


class BankAccount:
    def __init__(self, holder_name, balance, transactions):
        self.holder_name = holder_name
        self.balance = balance
        self.transactions = transactions

    def __str__(self):
        return f"Account holder: {self.holder_name}, Balance: {self.balance}"

    def __add__(self, other):
        return self.balance + other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __len__(self):
        return len(self.transactions)
acc1 = BankAccount("Alice", 5000, ["deposit", "withdraw", "deposit"])
acc2 = BankAccount("Bob", 5000, ["deposit", "deposit"])

# __str__
print(acc1)

# __add__
print("Total balance:", acc1 + acc2)

# __eq__
print("Same balance?", acc1 == acc2)

# __len__
print("Number of transactions:", len(acc1))
