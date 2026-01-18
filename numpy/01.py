# # What is NumPy?

# NumPy stands for Numerical Python.
# It is a core Python library used for:
# Working with numbers
# Handling large datasets
# Performing fast mathematical operations
# Doing scientific computing, data analysis, AI, ML

# Why Do We Need NumPy?
# Problem with Python Lists

# Python lists:
# Are slow for large calculations
# Cannot do vectorized math easily
# Consume more memory
# Example (Python List ❌)
# a = [1, 2, 3]
# b = [4, 5, 6]

# # This does NOT work
# a + b

# NumPy Solution ✅
# import numpy as np
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# a + b
# # Output: [5 7 9]
# 🔥 NumPy makes math easy, clean, and fast

# 1D Array (Vector)
# a = np.array([1, 2, 3])

# 2️⃣ 2D Array (Matrix)
# b = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# 3️⃣ 3D Array
# c = np.array([
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]]
# ])
import numpy as np
# arr = np.array([1, 2, 3, 4])
# type(arr)
# print(arr)
# print(arr.shape)  # Output: (4,)
# print(arr.dtype)  # Output: int64 (or int32 depending on your system)

# b = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(b)
# print(b.shape)  # Output: (2, 3)
# print(b.dtype)  # Output: int64 (or int32 depending on your system)
# print(b.ndim)  # Output: 2 (number of dimensions
# print(b.size)  # Output: 6 (total number of elements)
# print("item size",b.itemsize)  # Output: 8 (bytes per element for int64)



# C= np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])  
# print(C)    
# print(C.shape)  # Output: (3, 3)
# print(C.dtype)  # Output: int64 (or int32 depending on your system)

# d=np.arange(0, 10, 2)  # array([0, 2, 4, 6, 8])
# reshaped_d=d.reshape(5,1)  # Reshape to 5 rows, 1 column
# print(reshaped_d)
# print(d)


# e= np.ones((3, 4))  # 3x4 array of ones
# print(e)
# F=np.eye(3)  # 3x3 Identity matrix
# print(F)




# # Numpy vectorization example
# import numpy as np
# # Without NumPy
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
# result = []
# for i in range(len(list1)):
#     result.append(list1[i] + list2[i])  
# print("Without NumPy:", result)  # Output: [11, 22, 33, 44, 55]

# # With NumPy
# arr1 = np.array([1, 2, 3, 4, 5  ])
# arr2 = np.array([10, 20, 30, 40, 50])
# addititon = arr1 + arr2
# print("With NumPy:", addititon)  # Output: [11 22 33 44 55]
# subtraction = arr2 - arr1
# print("Subtraction With NumPy:", subtraction)  # Output: [ 9 18
# # 27 36 45]
# multiplication = arr1 * arr2
# print("Multiplication With NumPy:", multiplication)  # Output: [ 10 40 90 160 250]
# division = arr2 / arr1
# print("Division With NumPy:", division)  # Output: [10. 10. 10. 10. 10.]




# # universal functions (ufuncs) example
# unviersal_add = np.add(arr1, arr2)
# print("Universal function add:", unviersal_add)  # Output: [11 22 33 44 55]
# unviersal_subtract = np.subtract(arr2, arr1)    
# print("Universal function subtract:", unviersal_subtract)  # Output: [ 9 18 27 36 45]
# unviersal_multiply = np.multiply(arr1, arr2)
# print("Universal function multiply:", unviersal_multiply)  # Output: [
# square_root = np.sqrt(arr1)
# print("Universal function square root:", square_root)  # Output: [1.
# # 41421356 1.73205081 2. 2.23606798] 40 90 160 250] 
# unviersal_divide = np.divide(arr2, arr1)
# print("Universal function divide:", unviersal_divide)  # Output: [10
#     # 10. 10. 10. 10.]
# unviersal_exp = np.exp(arr1)
# print("Universal function exp:", unviersal_exp)  # Output: [ 2.71828183
# # 7.3890561 20.08553692 54.59815003 148.4131591]
# unviersal_log = np.log(arr2)    
# print("Universal function log:", unviersal_log)  # Output: [2.30258509




# # Slicing in numpy
# dim_array=np.array([[1,2,34,4,43],[22,3,4,55,2],[2,4,4,3,2]])
# print("slcign",dim_array[0][0])

# print(dim_array[1,2])
# print(dim_array[:,2])  # all rows, 2nd column
# print(dim_array[1,:])  # 1st row, all columns
# print(dim_array[0:2,1:4])  # rows 0-1, columns 1-3
# print(dim_array[::2,::2])  # every 2nd row and every 2nd column


# mean median standard deviation and varience
# Term	Meaning (Easy Words)
# Mean	Average value
# Median	Middle value
# Variance	How spread out the numbers are
# Standard Deviation	Average distance from the mean
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean = np.mean(data)
print("Mean:", mean)  # Output: 5.5
median = np.median(data)
print("Median:", median)  # Output: 5.5
std_dev = np.std(data)
print("Standard Deviation:", std_dev)  # Output: 2.872281323
variance = np.var(data)
print("Variance:", variance)  # Output: 8.25


# logical operations
arr = np.array([10, 15, 20, 25, 30])
greater_than_20 = arr[(arr > 20)& (arr<30)]
print("Greater than 20:", greater_than_20)  # Output: [25 30]


arr1=np.full((2,2), 7)
print(arr1)

arr2=np.linspace(0, 1, 5)
print(arr2)

arr23 = np.array([1,2,3,4,5,6])
arr23 = arr23.reshape(2,3)
print(arr23)