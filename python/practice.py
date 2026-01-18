# class SchoolAdmission:
#     def __init__(self,name,age,mobile_number):
#         self.name =name
#         self.age=age
#         self.mobile_number=mobile_number

#     def information(self):
#       print(f"this is {self.name} and age is {self.age} and mobile number is {self.mobile_number}")  

# p1=SchoolAdmission("Muhammad Nidal",11,"012901921021")
# p1.information()



class BankingSystem:
   def __init__(self,name,password):
      self.name=name
      self.__password=password


   def get_password(self):
      return  self.__password

         

b=BankingSystem("nidal",1)
print(b.name)
print(b.get_password())
# print(b.__password)

class BankingSystem:
   def __init__(self, name, password):
      self.name = name
      self.__password = password   # private password

   def get_password(self):
      return self.__password
   
   def set_password(self,updatedPassword):
      if updatedPassword > 0:
         self.__password = updatedPassword
         print("your password is update")
      else:
         print("your are not vlaid")
   
#    def set_password(self, new_password):
#       if new_password > 0:   
#          self.__password = new_password
#          print("Password updated successfully")
#       else:
#          print("Invalid password. Try again.")

     
   

# Example usage
b = BankingSystem("nidal", 1234)
print(b.name)             
print(b.get_password())   
print("we udpated your password  becuase your password is to much week")
b.set_password(123456)     
print(b.get_password())   



