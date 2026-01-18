
# What is Polymorphism?

# The word Polymorphism means "many forms".
# 👉 In Python, it allows us to use the same function/method name but with different behaviors depending on the object or arguments.


# class Animal:
#     def speak(self):
#         print("Animal makes a sound.")
# class DOg(Animal):
#     def speak(self):
#         print("Dog barks.")
# class Cat(Animal):
#     def speak(self):
#         print("Cat meows.")

# a= Animal()
# d = DOg()
# c = Cat()
# a.speak()  # Output: Animal makes a sound.                
# d.speak()  # Output: Animal makes a sound.                
# c.speak()  # Output: Animal makes a sound.          



# class Calculator:
#     def add(self,a=0,b=0,c=0):
#         return a + b + c
    
# calc=Calculator()
# print(calc.add(0))
# print(calc.add(3,4))  # Output: TypeError: add() takes 3 positional arguments but 4 were given
# print(calc.add(1,2,3))  # Output: 6


# class Calculator:
#     def add(self, *args):
#         return sum(args)

# calc = Calculator()
# print(calc.add(1, 2, 3))  # ✅ Output: 6
 

# Method Overriding
# method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.


class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")
class Cat(Animal):
    def speak(self):
        print("Cat meows.") 

a= Animal()
d = Dog()
c = Cat()
a.speak()  # Output: Animal makes a sound.
d.speak()  # Output: Dog barks.
c.speak()  # Output: Cat meows.
