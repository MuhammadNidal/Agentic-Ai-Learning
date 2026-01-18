# 1. Multithreading & Multiprocessing
# 👉 These are used for running multiple tasks at the same time.

# 🔹 Multithreading
# Runs multiple threads inside a single process.
# Good for I/O tasks (like downloading files, reading APIs, etc.).


# import threading
# import time

# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#         time.sleep(1)

# def print_letters():
#     for c in "abcde":
#         print(f"Letter: {c}")
#         time.sleep(1)
        
# def wait_me():
#     for w in "waitforme":
#         print(f"wait for me: {w}")
#         time.sleep(1)
# # Run both functions at the same time
# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letters)
# t3 =threading.Thread(target=wait_me)
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# print("Done!")



# Multiprocessing
# Runs multiple processes (each has its own memory).
# Good for CPU-heavy tasks (like calculations).



# import multiprocessing

# def square(n):
#     print(f"{n} squared is {n*n}")

# if __name__ == "__main__":
    # if __name__ == "__main__":

# This is very important in multiprocessing.
# On Windows, when Python starts a new process, it re-runs the whole file.
# Without this line, the program would get stuck in an infinite loop creating new processes
# 👉 So, if __name__ == "__main__": ensures that the multiprocessing code only runs in the main process, not in child processes.
    # numbers = [1, 2, 3, 4, 5]
    # processes = []

    # for num in numbers:
    #     p = multiprocessing.Process(target=square, args=(num,))
    #     processes.append(p)
    #     p.start()

    # for p in processes:
    #     p.join()







# import asyncio

# async def greet(name):
#     print(f"Hello {name}")
#     await asyncio.sleep(2)   # pretend waiting for data
#     print(f"Goodbye {name}")

# async def welcome(schoolName):
#     print(f"school information is bellow {schoolName}")
#     await asyncio.sleep(1)
#     print(f"this is another information {schoolName}")

# async def main():
#     await asyncio.gather(
#         greet("Nidal"),
#         greet("Ali"),
#         greet("Sara")
#     )
#     await asyncio.gather(
#         welcome("new islamia"),
#         welcome("mafas"),
#         welcome("kpk model school")
#     )

# asyncio.run(main())




# Create virtual environment
# python -m venv myenv  
# Activate
# myenv\Scripts\activate    # Windows
# deactivate
# source myenv/bin/activate # Mac/Linux
# Install libraries inside env
# pip install requests



import json 
nidal={
    "name":"nidal",
    "age":22,
    "information ":"very week mind set"

}

parse=json.dumps(nidal)
print(parse)


import json

data = {"name": "Nidal", "age": 22}

# Convert Python → JSON
json_str = json.dumps(data)
print(json_str)

assign=json.loads(json_str)
print(assign)


from datetime import datetime
time=datetime.now()
print("Formatted:", time.strftime("%Y-%m-%d %H:%M:%S"))

print(time)