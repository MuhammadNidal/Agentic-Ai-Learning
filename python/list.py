x=[]
print(type(x))
x=[1, 2, 3, 4, 5]
print(x)
print(type(x))
print(x[0])  # Accessing first element

x =[1,"ndial", 3.5, True]
print(x)

# nested list
nested_list = [1,2,3, [4, 5, 6], [7, 8, 9]]
print(nested_list[1])  # Accessing first sub-list
print(len(nested_list))


a=[1,3,5,7,8,9,3,1]
b=a[3]
c=a[-2]
print(c)
v = a[2:5]

f = a[:]
d=a[::2]
g=a[::-2]
print(g)


a = [0,1,2,3,4,5]
a[1:4] = ['x','y']   # [0,'x','y',4,5]
print(a)
a[2:2] = [7,8]       # insert at index 2 → [0,'x',7,8,'y',4,5]
print(a)
a[1:5] = []          # delete slice → [0,5]

print(a)




b=[3,2,1,4,5]
b.reverse()
print(b)
b.append(4)
b.append([4,2,4,6,9,1])

b.remove(2)
# b.sort()
a = ['Bob','alice','carol']
a.sort(key=str.lower)           # ['alice','Bob','carol'] (case-insensitive)
a.sort(key=len,reverse=True)
print(a)