# What Is a Generator in Python?

# A generator is a special type of function that:

# Returns values one at a time

# Does not store all values in memory

# Uses the yield keyword instead of return

# Generators are used for large data or infinite sequences.

# Generator vs Normal Function
# Normal Function

# Uses return

# Ends execution after returning a value

# Stores all values in memory (if list is used)

# Generator Function

# Uses yield

# Pauses execution and remembers its state

# Resumes from where it left off

# What Is yield?

# yield:

# Returns a value temporarily

# Pauses the function

# Saves local variables and execution state

# Continues execution on the next call

# Think of yield as:

# “Return this value now, I’ll continue later.”

# Simple Example: Generator vs Function
# Normal Function
# def normal():
#     return 1
#     return 2  # never executed

# Generator Function
# def generator():
#     yield 1
#     yield 2
#     yield 3

# How Generator Works Internally
# g = generator()

# print(next(g))  # 1
# print(next(g))  # 2
# print(next(g))  # 3


# After values finish:

# next(g)  # StopIteration

# Generator Example (Easy & Clear)
# Example 1: Print Numbers
# def numbers(n):
#     for i in range(n):
#         yield i


# Usage:

# for num in numbers(5):
#     print(num)


# Output:

# 0
# 1
# 2
# 3
# 4

# Generator Saves Memory (Important!)
# Without Generator (List)
# nums = [i for i in range(1000000)]

# With Generator
# nums = (i for i in range(1000000))


# ✔ Generator does not load all values at once

# Generator Expression

# Similar to list comprehension but uses ().

# gen = (x * x for x in range(5))

# print(next(gen))
# print(next(gen))

# Generator with yield (Real-Life Example)
# Reading Large File
# def read_file(file):
#     for line in file:
#         yield line


# Reads line by line, not entire file.

# Difference: yield vs return
# yield	return
# Pauses function	Ends function
# Remembers state	Loses state
# Multiple values	Single value
# Generator + Loop
# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1


# Usage:

# for i in countdown(3):
#     print(i)

# Generator is an Iterator

# Generator automatically implements:

# __iter__()

# __next__()

# That’s why it works with for loop

# When to Use Generators?

# ✔ Large datasets
# ✔ Infinite sequences
# ✔ Streaming data
# ✔ Memory efficiency
# ✔ Performance improvement

# Problem

# An ATM has many transactions.
# We want to process them one by one, without loading all at once.
# This is a perfect use case for a generator.
# Generator Function


def atm_transactions(transactions):
    for tx in transactions:
        yield tx
transactions = [
    "Deposit 1000",
    "Withdraw 500",
    "Withdraw 200",
    "Deposit 300"
]

gen = atm_transactions(transactions)

print(next(gen))  # First transaction
print(next(gen))  # Second transaction
