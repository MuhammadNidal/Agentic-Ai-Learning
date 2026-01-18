# 🔹 Tuples in Python

# A tuple is an ordered, immutable sequence of elements.

# Like a list, but cannot be changed once created.

# # Useful when you need fixed collections (e.g., coordinates, database records).

# imutable and mutable main difference 

# mutable  once created can be changed
# immutable once created cannot be changed


t1=(1, 2, 3)  # A simple tuple
print(type(t1))  # Output: <class 'tuple'>
print(t1)  # Output: (1, 2, 3)
t2 = (1, "nidal", 3.5, True)  # A tuple with mixed types
print(t2)  # Output: (1, 'ndial', 3.5
t4=()
print(t4)  # Output: ()
t5=(1,)  # A single-element tuple (note the comma)
print(t5)  # Output: 1 (not a tuple, just an int)

t6=1,2,3,4,5,6
print(t6)  # Output: (1, 2, 3, 4, 5, 6)


t=(1, 2, 3, 4, 5, 6,7, 8 )  # Nested tuple
print(t[1])  # Accessing second element: Output: 2
print(len(t))  # Length of the tuple: Output: 8
print(t[:5])
print(t[2:5])  # Slicing the tuple: Output: (3, 4, 5)
# print(t[-1])


t = (1, [2, 3], 4)
t[1][0] = 99
print(t)  # (1, [99, 3], 4) ✅ list inside tuple is mutable


t = 1, 2, 3   # packed into tuple
print(t)      # (1, 2, 3)


a, b, c = (1, 2, 3)
print(a, b, c)   # 1 2 3

a,*b = (1, 2, 3, 4, 5)
print(a,b)  # 1


t=(1, 2, 3, 4, 5)
print(t.count(2))  # Count occurrences of 2: Output: 1
print(t.index(3))  # Index of first occurrence of 3: Output: 2



# ✅ 8. Comparison with Lists
# Feature	List	Tuple
# Syntax	[1,2,3]	(1,2,3)
# Mutable	✅ Yes	❌ No
# Methods	Many (append, remove, …)	Only count, index
# Performance	Slightly slower (mutable overhead)	Fast
# 
# er, lightweight
# Use case	Changeable data	Fixed data / dictionary key


import sys
list1 = [1,2,3]
tuple1 = (1,2,3,4)

print(sys.getsizeof(list1))   # e.g. 104


print(sys.getsizeof(tuple1))  # e.g. 88



def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# 1️⃣ Tuple Concatenation ➕

# Joining two or more tuples.

# t1 = (1, 2)
# t2 = (3, 4)
# result = t1 + t2
# print(result)
# Output:
# (1, 2, 3, 4)
# 2️⃣ Tuple Multiplication ✖️

# Repeating a tuple multiple times.
# t = (1, 2)
# print(t * 3)
# Output:

# (1, 2, 1, 2, 1, 2)

# 3️⃣ Tuple Methods 🧰

# Tuples have only 2 methods:
# 🔹 count()
# Counts how many times a value appears.

# t = (1, 2, 2, 3)
# print(t.count(2))
# Output:

# 2
# 🔹 index()
# Returns index of first occurrence.

# t = (10, 20, 30)
# print(t.index(20))
# Output:
# 1

# 4️⃣ Packing Tuple 📦

# Putting multiple values into one tuple.

# data = 10, 20, 30
# print(data)


# Output:

# (10, 20, 30)

# 5️⃣ Unpacking Tuple 🎁

# Extracting values from a tuple.

# t = (1, 2, 3)
# a, b, c = t

# print(a, b, c)
# Output:
# 1 2 3
# 6️⃣ Unpacking with Star Operator ⭐

# Used when you don’t know exact number of values.
# t = (1, 2, 3, 4, 5)
# a, *b, c = t

# print(a)
# print(b)
# print(c)

# Output:

# 1
# [2, 3, 4]
# 5
# 👉 *b stores multiple values as a list

# 7️⃣ Nested Tuple 🪆

# Tuple inside another tuple.
# t = (1, 2, (3, 4), 5)
# print(t[2])

# Output:

# (3, 4)
# Access Nested Value
# print(t[2][1])
# Output:
4
