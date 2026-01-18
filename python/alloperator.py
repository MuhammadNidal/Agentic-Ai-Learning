# Arithmetic Operators

a = 30
b= 20
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division which gives float result
print(a % b)  # Modulus  reminder
print(a // b)  # Floor Division which gives integer result

print(a ** b)  # Exponentiation



#  2. Comparison (Relational) Operators


a = 10
b = 20
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to


# ✅ 3. Logical Operators


a = True
b = False
print(a and b)  # Logical AND
print(a or b)   # Logical OR
print(not a)    # Logical NOT


# ✅ 4. Assignment Operators
a = 10
b = 20
a += b  # a = a + b
print(a)  # 30
a -= b  # a = a - b     
print(a)  # -10 
a *= b  # a = a * b
print(a)  # -200
a /= b  # a = a / b
print(a)  # -10.0
a %= b  # a = a % b
print(a)  # -10.0
a //= b  # a = a // b
print(a)  # -1.0




# ✅ 5. Membership Operators
text = "Hello, World!"
print('Hello' in text)  # True
print('Python' not in text)  # True



# ✅ 6. Identity Operators
x = [1,2,3,4,5]
y=x
z =[1,2,3,4,5]
print(x is z)
print(y is not z)
print(x is y)  # True, because y is the same object as x
print(x == z)  # True, because they have the same content