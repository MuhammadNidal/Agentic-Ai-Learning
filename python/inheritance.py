

#  Inheritance


# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} makes a sound.")
# class Dog(Animal):
#     def speaking(self):
#         print(f"{self.name} barks.")


# d=Dog("Buddy")
# d.speak()  # Output: Buddy barks.       
# d.speaking()  



class Father:
    def skill(self):
        print("Father's skills: Cooking, Driving")

class Mother:
    def skills(self):
        print("Mother's skills: Teaching, Gardening") 

class Child(Father, Mother):
    def extra_skills(self):
        print("Child's skills: Coding, Gaming")

c=Child()
c.skills()  # Output: Father's skills: Cooking, Driving
c.skill()  # Output: Father's skills: Cooking, Driving
c.extra_skills()  # Output: Child's skills: Coding, Gaming




# class Grandfather:
#     def __init__(self, name):
#         self.name = name
# class Father(Grandfather):
#     def __init__(self, name, age):
#         super().__init__(name)  # Call the constructor of Grandfather
#         self.age = age        
# class Child(Father):
#     def __init__(self, name, age, hobby):
#         super().__init__(name,age)  # Call the constructor of Father
#         self.hobby = hobby
# d=Child("Nidal", 23, "Coding")
# print(d.name)  # Output: Nidal  
# print(d.age)   # Output: 23
# print(d.hobby)  # Output: Coding




class Hondacvic:
    def __init__(self,wheel,engine,color):
        self.wheel = wheel  
        self.engine = engine
        self.color = color
    def greetCar(self):
        print(f"this is my Honda Civic with {self.wheel} wheels")    

class LocalCar(Hondacvic):
    def __init__(self,wheel,engine,price,color):
        super().__init__(wheel,engine,color) 
        self.price = price
    def showPrice(self):
        print(f"the price of my car is {self.price}")       

CivicCar= LocalCar(4,"V4",25000,"Red")
CivicCar.greetCar()  # Output: this is my Honda Civic with 4  
CivicCar.showPrice()  # Output: the price of my car is 25000      