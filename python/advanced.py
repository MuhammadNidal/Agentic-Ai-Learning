from functools import wraps

def log_calls(func):
    @wraps(func)  # preserves name, docstring, annotations
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__}({args=}, {kwargs=})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} -> {result!r}")
        return result
    return wrapper

@log_calls
def add(a, b):
    "Add two numbers."
    return a + b

print(add(22,22))




def repeat(n=1):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return deco

@repeat(n=3)
def greet(name): print(f"Hello, {name}!")

print(greet("nidal"))






import itertools as it

nums = [1, 2, 3, 4]

lis123=list(it.accumulate(nums))   
print(lis123)
print(list(it.chain([1,2], [3,4])) )



def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, name="Nidal", age=22)
