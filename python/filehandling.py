# f = open("example.txt", "r")

# print(f.read())         # read entire file
# print(f.read(10))       # read first 10 characters
# print(f.readline())     # read one line
# print(f.readlines())    # read all lines into a list

# f.close()




f = open("nidal.txt", "w+")
f.write("Hello, this is Python!\n")
f.write("File handling is easy.")
f.close()



# f = open("example.txt", "a")
# f.write("\nNew line added at the end.")
# f.close()
