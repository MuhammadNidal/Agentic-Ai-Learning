
# Encapsulation
# Encapsulation means hiding the internal details of an object and only exposing what is necessary.
# It allows us to protect variables and methods from direct access/modification.
# In Python, encapsulation is done using:
# Public variables/methods → accessible everywhere.
# Protected variables/methods → single underscore _var (convention, "should not be accessed directly").
# Private variables/methods → double underscore __var (name mangling, makes it hard to access directly).


class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age # Protected variable
    def _display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")    

p1= Person("Nidal", 23)
p1._display_info()  # Output: Name: Nidal, Age: 23



class Teacher: 
    def __init__(self,name ,education):
        self._name = name
        self._education = education
    def __display_info(self):
        print(f"Name:{self._name}and education is {self._education}")

    def show_info(self):               # public method (to access private method)
        self.__display_info()   

t1 = Teacher("Nidal", "BS Computer Science")
# t1.__display_info()  # This will raise an AttributeError because __display_info is private
t1.show_info()  # ❌ AttributeError
print(t1)




class Manager:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def show_Info(self):
        print(f"{self.__name} and age is {self.__age}")    

p2=Manager("ndial",11)
p2.show_Info()        
print(p2)


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private

    # Getter (read balance safely)
    def get_balance(self):
        return self.__balance

    # Setter (update safely)
    def set_balance(self, amount):
        if amount < 0:
            print("❌ Balance cannot be negative!")
        else:
            self.__balance = amount

# Usage
account = BankAccount(1000)
print(account.get_balance())   # 1000

account.set_balance(1500)      # ✅ Updates
print(account.get_balance())   # 1500


