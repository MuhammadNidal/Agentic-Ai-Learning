# Error Handling in Python
# Errors are unexpected situations that occur during program execution.
# If we don’t handle them, Python will stop the program with an error message (called a traceback


try:
    int("abc")  # This will raise a ValueError
except ValueError as e: 
    print(f"ValueError occurred: {e}")
except TypeError as e:  # Catching a different type of error
    print(f"TypeError occurred: {e}")
else:
    print("No errors occurred, this block runs if try is successful.")

try:
    f = open("test.txt", "w")
    f.write("Hello")
except Exception as e:
    print("Error:", e)
finally:
    f.close()   # always executed
    print("File closed")

x = -5
if x < 0:
    raise ValueError("x cannot be negative")
