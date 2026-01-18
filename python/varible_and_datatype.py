x = 10
print(x)
y = 20
print(y)
z = x + y
print(z)


z = 30
print(type(z))

z= "30"
print(type(z))

muhammad = "Ali"
print(muhammad)
muhammad1 = "Ahmed"
print(muhammad)
combined = muhammad +" "+muhammad1
print(combined)

muhammad.upper()
print(muhammad.upper())
muhammad = muhammad.upper()
print(muhammad)

muhammad = muhammad.lower()
print(muhammad)

muhammad = muhammad[1]
print(muhammad)

muhammad = muhammad[0:2]
print(muhammad)


float_number = 10.5
print(float_number)

z = 2+22j
print(z)
print(type(z))
print(z.real)
print(z.imag)




is_active = True
is_open = False

print(10 < 5)   # True
print(5 == 3)   # False
print(type(is_active))  # <class 'bool'>



x = None
print(x)          # None
print(type(x))    # <class 'NoneType'>

def func():
    return None

print(func())     # None



x=12
print(type(x))  # <class 'int'>
print(int(x))  # 12
print(float(x))  # <class 'float'>
print(str(x))  # '12'

print(isinstance(x,float))