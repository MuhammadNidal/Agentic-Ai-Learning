# What Is Custom Exception Handling?

# Custom exception handling means creating your own exception classes to represent specific error conditions in your program.
# Instead of using only built-in exceptions like:
# ValueError
# TypeError
# ZeroDivisionError
# you define your own meaningful exceptions.
# Why Use Custom Exceptions?
# Custom exceptions help to:
# Make error messages clear and specific
# Handle application-specific errors
# Improve readability and debugging
# Separate normal logic from error logic
# Write clean and maintainable code





class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        super().__init__(
            f"Insufficient balance! Balance: {balance}, Requested: {amount}"
        )

class InvalidAmountError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")

        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)

        self.balance -= amount
        print("Withdrawal successful. Remaining balance:", self.balance)


account = BankAccount(3000)

try:
    account.withdraw(1000)
except InvalidAmountError as e:
    print("Invalid Amount:", e)
except InsufficientBalanceError as e:
    print("Balance Error:", e)
except Exception as e:
    print("Unknown Error:", e)





# Iterators and Generators in Python


# An iterator is an object that allows you to traverse elements one by one from a collection (like a list or tuple).
# Key Points
# An iterator follows the iterator protocol
# It must implement:
# __iter__() → returns the iterator object
# __next__() → returns the next value
# When elements are finished, it raises StopIteration

nums = [1, 2, 3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # StopIteration Error

try:
    print(next(it))  # This will raise StopIteration
except StopIteration:   
    print("Reached the end of the iterator.")