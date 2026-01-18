s={1,2,3,4,5,6,7,8}  # A simple set
print(s)

s2=([1,2,3,4,5,6,7,8])  # A set with mixed types
print(s2)
s.add(3)        # {1,2,3}  (add one item)
s.update([3,4]) # {1,2,3,4} (add many from any iterable)
print(s)

s.remove(4)     # removes 4; KeyError if not present
print(s)
s.discard(4)    # no error if 4 missing (safe)
print(s)
s.pop()         # removes & returns an arbitrary element; KeyError if empty
print(s)
s.copy() 
print(s) 
s.clear()       # becomes empty set()
print(s)

 # Output: {1, 2, 3, 5, 6, 7, 8}
