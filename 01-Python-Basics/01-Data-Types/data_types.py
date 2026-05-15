# Diclare Variables

name = "Sagar Nautiyal"
age = 20
marks = 99.9
isTrue = True

print(f"Name is {name}, and data type is {type(name)}")
print(f"Age is {age}, and data type is {type(age)}")
print(f"Marks is {marks}, and data type is {type(marks)}")
print(f"Boolean is {isTrue}, and data type is {type(isTrue)}")

# Type Casting 

num1 = "12"
num2 = 10 

# Without Type Cating

#print(num1 + num2) 

# Here we have show error because num1 is a string and num2 is a integer 
# now with Type casting 
print(int(num1) + num2)