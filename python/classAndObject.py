# # class and objects

class Person:
    pass
p=Person()
print(p)

class Student7777777777778:
    pass
s=Student7777777777778()
print(s)


class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age      
    def bark(self):
        print(f"{self.name} is barking.")

d=Dog("Buddy", 3)
d.bark()  # Output: Buddy is barking.
d1=Dog("Buddy1", 3)
d2=Dog("Buddy2", 3)
print(d2.name)
print(d2.age)



class student:
    def __init__(self,stdName,stdFees):
        self.name=stdName
        self.fees=stdFees
    
    def addFess(self,amount):
        self.fees +=amount
        
    def reminFees(self,amount):
        self.fees -=amount 

s1=student("Nidal", 5000)
print(s1.fees)

s1.addFess(2000)
print(s1.fees)

s1.reminFees(1000)
print(s1.fees)



# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print(f"Hello ,my name is {self.name} and  i am {self.age} years old.")
# a=Person("kamran", 23)
# a.greet()  # Output: Hello, my name is kamran and I am 23 years old.
# p = Person("Nidal", 23)
# n=Person("Ali", 30)
# n.greet()  # Output: Hello, my name is Ali and I am 30 years old.
# p.greet()  # Output: Hello, my name is Nidal and I am
# print(p.name)  # Output: Nidal
# print(p.age)   # Output: 23
# print(p)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = None
#         self.age = age          # go through property for validation

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError("age must be >= 0")
#         self._age = value
# p1= Person("Nidal", 23)
# print(p1.age)  # Output: 23



# class Person:
#     def __init__(self, name, age):
#         self.name, self.age = name, age
#     def __repr__(self):
#         return f"Person(name={self.name!r}, age={self.age})"
#     def __str__(self):
#         return f"{self.name} ({self.age})"

# p = Person("Nidal", 23)
# print(repr(p))  # Person(name='Nidal', age=23)
# print(p)        # Nidal (23)
# # 










# Encapsulation
# Encapsulation means hiding the internal details of an object and only exposing what is necessary.
# It allows us to protect variables and methods from direct access/modification.
# In Python, encapsulation is done using:
# Public variables/methods → accessible everywhere.
# Protected variables/methods → single underscore _var (convention, "should not be accessed directly").
# Private variables/methods → double underscore __var (name mangling, makes it hard to access directly).


# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age # Protected variable
#     def _display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")    

# p1= Person("Nidal", 23)
# p1._display_info()  # Output: Name: Nidal, Age: 23



# class Teacher: 
#     def __init__(self,name ,education):
#         self._name = name
#         self._education = education
#     def __display_info(self):
#         print(f"Name:{self._name}and education is {self._education}")

#     def show_info(self):               # public method (to access private method)
#         self.__display_info()   

# t1 = Teacher("Nidal", "BS Computer Science")
# # t1.__display_info()  # This will raise an AttributeError because __display_info is private
# t1.show_info()  # ❌ AttributeError
# print(t1)




# class Manager:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def show_Info(self):
#         print(f"{self.__name} and age is {self.__age}")    

# p2=Manager("ndial",11)
# p2.show_Info()        
# print(p2._Manager__name)


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private

#     # Getter (read balance safely)
#     def get_balance(self):
#         return self.__balance

#     # Setter (update safely)
#     def set_balance(self, amount):
#         if amount < 0:
#             print("❌ Balance cannot be negative!")
#         else:
#             self.__balance = amount

# # Usage
# account = BankAccount(1000)
# print(account.get_balance())   # 1000

# account.set_balance(1500)      # ✅ Updates
# print(account.get_balance())   # 1500




# # What are Magic Methods in Python?

# # Magic methods (also called dunder methods) are special methods in Python.
# # They start and end with double underscores (__).
# # Python automatically calls them in certain situations (you don’t call them directly most of the time).

# # 👉 Example:
# # __init__ is called when you create an object.
# # __str__ is called when you print an object.
# # __len__ is called when you use len(object).


# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

# s1 = Student("Nidal", 101)  # __init__ called
# print(s1.name)  # Nidal



# class Classroom:
#     def __init__(self, students):
#         self.students = students
    
#     def __len__(self):
#         return len(self.students)

# c1 = Classroom(["Nidal", "Ali", "Sara"])
# print(len(c1))  # __len__ → 3


# class Classroom:
#     def __init__(self, students):
#         self.students = students
    
#     def __len__(self):
#         return len(self.students)

# c1 = Classroom(["Nidal", "Ali", "Sara"])
# print(len(c1))  # __len__ → 3



# class Book:
#     def __init__(self, pages):
#         self.pages = pages
    
#     def __add__(self, other):
#         return self.pages + other.pages

# b1 = Book(100)
# b2 = Book(200)
# print(b1 + b2)  # __add__ called → 300



# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def __eq__(self, other):
#         return self.name == other.name

# p1 = Person("Nidal")
# p2 = Person("Nidal")
# print(p1 == p2)  # True (because __eq__ compares names)
