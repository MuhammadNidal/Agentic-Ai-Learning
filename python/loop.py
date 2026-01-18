for i in range(10):
    print(f"Iteration {i}")


for i in range(1, 11):
    print(f"Number: {i}")    


names = ["Ali", "Nidal", "Sara"]
for idx, name in enumerate(names, start=1):
    print(idx, name)    # 1 Ali, 2 Nidal, 3 Sara

# 4) zip: iterate in parallel
first = [1, 2, 3]
second = [10, 20, 30]
for a, b in zip(first, second):
    print(a, b)         # (1,10), (2,20), (3,30)

for ch in "python":
    print(ch)          # p, y, t, h, o, n

# while loop
count = 0 
while count < 5:
    print(f"Count is {count}")
    count += 1
  
adding =9
while adding <20:
    print(adding)
    adding += 1

for n in range(1, 11):
    if n==5:
        print("Reached 5, breaking loop")
        break

for n in range(1, 8):
    if  n == 5:
        print("Reached 5, skipping to next iteration")
        break  
    
    
    
for n in range(1, 8):
    if n == 5:
        print("Reached 5, skipping to next iteration")
        continue
    print(n)  # Will skip printing 5


for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")  # Will print odd numbers  

# pass — do nothing (placeholder)

# Use when syntax requires a block but you don’t want any action yet.

# for n in range(3):
#     pass  # TODO: implement later


for i in range(1,5):
    for j in range(1, 4):
        # print(f"i: {i}, j: {j}")  # Nested loop example
        print(i, j)  # Will print pairs (1,1), (1,2), ..., (4,3)