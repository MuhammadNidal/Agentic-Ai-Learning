# .

# 🐼 What is Pandas?
# Pandas is a powerful Python library used for:
# Data analysis
# Data cleaning
# Data manipulation

# Working with structured data (tables)
# It is built on top of NumPy and is widely used in:
# Data Science
# Machine Learning
# Backend data processing
# CSV / Excel / JSON handling
# API data analysis


# The name "Pandas" is derived from "Panel Data", an econometrics term for multidimensional structured data.
# data manipulation and analysis library

# Data Manipulation:
# is a library providing data structures and functions needed to manipulate structured data seamlessly.
# It is built on top of NumPy and is designed to work efficiently with large datasets.
# Pandas introduces two primary data structures: Series and DataFrame.
# fixing errors in data, handling missing values, and reshaping datasets.

# Data Analysis:
# Pandas offers a wide range of tools for data analysis, including data cleaning, transformation,
# aggregation, and visualization.
# It provides functions for grouping data, performing statistical operations, and generating summary statistics.
# Pandas also integrates well with other data analysis libraries in Python, such as Matplotlib and Seaborn,
# making it easier to visualize and interpret data.


import pandas as pd
# by default, the index will be 0, 1, 2, ...

# s=pd.Series([1, 3, 5, 7, 9])
# print(s)    


# data = {'a': 10, 'b': 20, 'c': 30}
# s2 = pd.Series(data)
# print(s2)

# s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)

# df = pd.DataFrame({
#     "name": ["Ali", "Sara", "Ahmed"],
#     "age": [23, 21, 25]
# })
# print(df)


# df=pd.read_csv("recipe_template.csv")
# print(df)


# f=pd.DataFrame({"A":[1,2], "B":[3,4]})
# f=pd.Series([1,2,3])
# print(f)


# df.head()        # first 5 rows
# df.tail()        # last 5 rows
# df.shape         # (rows, cols)
# df.columns       # column names
# df.dtypes        # data types
# df.info()        # summary (nulls, types, memory)
# df.describe()    # stats for numeric columns


# Data selection
# print(df["title"])          # single column
# print(df[["title", "description"]])  # multiple columns
# print(df.iloc[0])        # first row by position
# print(df.loc[0])         # first row by label
# print(df.iloc[0:5])     # first 5 rows
# print(df[df["rating"] > 4.5])  # filter rows


# d2 =pd.DataFrame({
#     "X": [1, 2, 3],
#     "Y": [4, 5, 6]
#     })  

# print(d2)
# d2.to_csv("my_data.csv", index=False)
# d2.to_json("my_data.json", index=False)
# d2.to_excel("my_data.xlsx", index=False)




# df22=pd.read_csv("recipe_template.csv")
# # print(df22.head())
# # print(df22.tail())
# # print(df22.info())
# print(df22.describe())



# df2=pd.read_json("file.json")
# print(df2)
# # print(df2.head())
# # print(df2.info())     
# print(df2.describe())
# print(df2.shape)



# ages = pd.Series([25, 30, 35, 40])
# print(ages)

# ages = pd.Series([25, 30, 35], index=["Ali", "Sara", "Usman"])
# print(ages)


# if the company give you the dataset to find the average age of employees
ages = pd.Series([25, 30, 35, 40,50,60,70,80,90,100])
# sum of all ages / number of employees
# 2050 / 10
# result: 57.5
average_age = ages.mean()
print("mean of employees:", average_age)
# Output: Average age of employees: 57.5

median_age = ages.median()
print("Median age of employees:", median_age)
# Output: Median age of employees: 60.0
age_std = ages.std()
print("Standard Deviation of ages:", age_std)
# Output: Standard Deviation of ages: 25.81988897471611
age_variance = ages.var()
print("Variance of ages:", age_variance)
# Output: Variance of ages: 666.6666666666666
min_age = ages.min()
print("Minimum age:", min_age)
# Output: Minimum age: 25
max_age = ages.max()
print("Maximum age:", max_age)
age_count = ages.count()
print("Count of ages:", age_count)


