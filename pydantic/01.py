# Pydantic is a Python library used to:

# ✅ Check data
# ✅ Validate data
# ✅ Convert data into the correct type
# ✅ Make your code safe and clean

# Pydantic makes sure the data you receive is correct, clean, and usable.
# It is very popular in:
# FastAPI
# APIs
# Backend systems
# Data validation


# Without Pydantic ❌
# user = {
#     "name": "Ali",
#     "age": "25"
# }
# print(user["age"] + 5)  # ❌ Error


from pydantic import BaseModel, ValidationError
class User(BaseModel):
    name: str
    age: int


User1=User(name="Ali", age="25")
print(User1.age + 5)  # Output: 30    

# Dataclass
from pydantic.dataclasses import dataclass
@dataclass
class Product:          
    id: int
    name: str
    price: float
p = Product(id="101", name="1111", price="999.99")
print(p.price + p.id + 50)  # Output: 1150.99



# model with optional field
from typing import Optional
class User(BaseModel):
    name: str
    age: Optional[int] = None   
User(name="Sara")  # ✅ OK
User(name="Ahmed", age=30)  # ✅ OK





# conditions
from pydantic import Field

class User(BaseModel):
    name: str
    age: int = Field(gt=18, lt=60)

User(name="Ali", age=25)   # ✅ OK
User(name="Sara", age=15)  # ❌ Error

# Rules:
# gt → greater than
# lt → less than
# min_length
# max_length



from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    name: str
    marks: int

try:
    s = Student(name="Sara", marks="abc")
except ValidationError as e:
    print(e)
# Output:
# 1 validation error for Student    
# 
# 
# 
    
from pydantic import BaseModel, EmailStr

class Account(BaseModel):
    email: EmailStr

Account(email="test@gmail.com")   # ✅
Account(email="wrong-email")      # ❌
