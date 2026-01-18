def greet():
    '''
    This function prints a greeting message.
    '''
    print("Hello, welcome to the program!")

greet()    

def adding(a,b):
    '''
    This function returns the sum of two numbers.
    '''
    return a + b    
print(adding(1,5))


def guest(name="Guest"):
    '''
    This function greets a user by name.
    If no name is provided, it defaults to "Guest".
    '''
    print(f"Hello, {name}!")

print(guest("Nidal"))
print(guest())  # Will use the default name "Guest"    

# Variable-length arguments
# 1) Positional arguments

def sum_all(*args):
    print("Arguments received:", args)
    return sum(args)
print(sum_all(1, 2, 3))  # Output: 6

def sunm_all(*args):
    for num in args:
        print(num)
print(sunm_all(4,5,6,7,"nidal"))


# Keyword arguments
def personal_info(**kwargs):
    print("Keyword arguments received:", kwargs)
    for key,value in kwargs.items():
        print(f"{key}: {value}")
personal_info(name="Nidal", age=23, city="Peshawar")        



# postional and keyword arguments
def details(*args,**kwargs):
    for item in args:
        print(f"this is the positive {item}")
    for key, value in kwargs.items():
        print(f"this is the key value pair {key}: {value}")    

print(details(1,23,4,5,6, age=23, name="nidal", city="Peshawar"))
def calculate(a, b):
    return a+b, a-b, a*b

x, y, z = calculate(10, 5)
print(x, y, z)  # Output: 15 5 50



def square(num):
    """This function returns the square of a number."""
    return num ** 2

print(square.__doc__)



square =lambda x:x*2
print(square(5))  # Output: 10
triple = lambda x: x*3
print(triple(4))  # Output: 12


subtract= lambda a,b:a-b
print(subtract(10, 5))  # Output: 5


nums=[1, 2, 3, 4, 5]
squared_num=list(map(lambda x:x**2, nums    ))
print(squared_num)  # Output: [1, 4, 9, 16, 25]




# Lambda with filter()
# anaynomous function  is the function without name
# lambda have the only arguement expression
# parameter we pass to the function

addition=lambda a,b:a*4
print(addition(2,3))  # Output: 20 




# Map Function
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

number1=[1,2,3,4]
number2=[10,20,30,40]
summed_numbers=list(map(lambda x,y:x+y,number1,number2))
print(summed_numbers)  # Output: [11, 22, 33,

words = ["apple", "banana", "cherry", "date"]
uppercased_words = list(map(lambda x: x.upper(), words))
print(uppercased_words)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'DATE']


# Filter Function in python
def even_numbers(num):
    return num % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(even_numbers, numbers))
print(even_nums)  # Output: [2, 4, 6]

# number that greate than 5
numbers = [3, 7, 2, 9, 4, 6]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  # Output: [7, 9, 6