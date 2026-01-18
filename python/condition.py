name= "nidal"
age = 23

if age<17 and name=="nidal":
    print(f"{name} is an adult."    )
elif age>17 and name=="nidal":
    print(f"{name} is a minor.")
else:
    print(f"{name} is not an adult.")


age = 23
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")    

citizen= "Pakistan"
c="pakistan zindabad" if citizen=="Pakistan" else "not a citizen"
print(c)  # Output: pakistan zindabad