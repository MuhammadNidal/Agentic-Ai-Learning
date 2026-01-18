import math
print(math.sqrt(16))  # Output: 4.0

print(math.pi)  # Output: 3.141592653589793

from math import sqrt, pi
print(sqrt(25))  # Output: 5.0
print(pi)  # Output: 3.141592653589793
# from math import sqrt,pi

# print(sqrt(16))  # Output: 4.0
# print(pi)  # Output: 3.141592653589793


import random
print(random.random())  # Output: Random float between 0.0 and 1.0
print(random.randint(1, 10))  # Output: Random integer between 1 and 10
numbers = [1, 2, 3, 4, 5]
print(random.choice(numbers))  # Output: Randomly selects an element from the list
print(random.sample(numbers, 3))  # Output: Randomly selects 3 unique elements from the list
print(random.shuffle(numbers))  # Shuffles the list in place


import datetime
print(datetime.datetime.now())  # Output: Current date and time
print(datetime.date.today())  # Output: Current date
# print(datetime.datetime.timezone.utc)  # Output: UTC timezone


import os
print(os.getcwd())  # Output: Current working directory
print(os.listdir())  # Output: List of files and directories in the current directory
# print(os.path.exists("modules.py"))  # Output: True if the file exists
# print(os.path.join("modules.py", "dicationary.py"))  # Output: Joins paths
# print(os.mkdir("new_directory"))  # Creates a new directory named "new_directory"
# print(os.fold("new_directory"))  # Removes the directory named "new_directory"
# print(os.rename("modules", "moduleandpackages"))  # Renames the directory


import sys
print(sys.version)  # Output: Python version information
print(sys.path)  # Output: List of directories Python searches for modules
print(sys.platform)  # Output: Platform information
print(sys.modules)  # Output: Dictionary of loaded modules
print(sys.exit(0))  # Exits the program with status code 0

# print("Arguments:", sys.argv)   # e.g., ["script.py", "arg1", "arg2"]



# import tuple

# print(tuple.add(5, 3))      # 8
# print(tuple.multiply(4, 2)) # 8


data=[1, 2, 3, 4, 5]
iter_data = iter(data)  # Create an iterator from the list
print(next(iter_data))  # Output: 1 
print(next(iter_data))  # Output: 2



# custom module creation