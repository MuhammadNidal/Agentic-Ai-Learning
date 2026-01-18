# What is Abstraction in Python?

# Abstraction means hiding the internal details and showing only what is necessary to the user.

# 👉 In simple words:
# You know WHAT a thing does, not HOW it does it.

# Real-Life Example 🚗
# Think about driving a car:
# You use:
# Steering
# Accelerator
# Brake
# You don’t know:
# How the engine works
# How fuel is injected
# How gears move internally
# This is abstraction.


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick")
c = Car()
c.start()  # Output: Car starts with a key
b = Bike()
b.start()  # Output: Bike starts with a kick    