# Print Statement 

# Computer Program --> 2 Streams 
# Input Stream --> From Programmer to the Computer 
# Output Stream --> From Computer to the Programmer 

# Output Stream --> Print Statement 
# Python is a Case Sensitive Language 
# Print vs print --> Differences "Print" -- throw an error 
# print --> Reserved Function / Predefined Function 
# Integer --> .... , -2 , -1 , 0 , 1 , 2 , ... 
# Float --> all decimals are also included and 
#           always included decimal point 
#                   Integer 2 = float 2.0 
# Character --> a letter --> Alpha Numeric --> Can contain letters, 
# numbers and also some special characters 
# string --> Sequence of Characters --> Difference making is quotes 
# Example: '123', "ABCD", "Hello World!!!", "Take off", "Hello 123456"

print("Hello World!!!") 
#For running the program F5 
# One Print Statement occupies the entire line 
print("Welcome to Programming World!!!")

print("Hello World!!!" , end = "")
print("Welcome to Programming World!!! (In Single Line)")

print("Hello World!!!" , end = " ")
print("Welcome to Programming World!!! (In Single Line with space)")

print("Hello World!!!" , end = "****")
print("Welcome to Programming World!!! (In Single Line)")

# Multiple Strings in One Command 
print("Hello World!!!","Welcome to Programming World!!!")
# 1st --> Printed in Single Line; combining two or more strings is called 
# as String Concatenation 
# 2nd --> Added space between the strings (Heppens always when you use "," based concatenation)
print(1) # We ve given integer data 
print("1") # We ve given character / string data 

# Another type of concatenation 
print("Hello World!!!"+"Welcome to the World of Programming Language!!!")
# Observation: without space 
#print("Hello World!!!!" + 1) --> Throws error because of string is concatenated with integer 
print("Hello World!!!!" + "1")

print(1 + 5)
print("1 + 5")

# Usage of Variables 
var = "Hello World!!!" # var is a variable with allocated memory 
# Memory Address of the String 
print(id(var))
print(var)
var = "Welcome!!!"
print(var)

# Data type stored in a variable  
# type() 
print(type(var))
# <class 'str'> --> 'str' corresponds to  String Data Type 
i = 10.0
print(i)
print(type(i))
print("hello world",i)

print("hello world" + str(i))

# F-String --> Formatted String 
# f"Text"
# It could variables 
# f"{var} {i}"
print(f"{var} {i}") # Variables should be placed inside the curly brace 

# Type Specifiers 
# %d --> Integer 
# %s --> String 
# %f --> Float 
print("Using Data Type Specifiers %s %f"%(var, i))

print("%s"%var)

print("%s %f %s"%(var, i, i))

#print("%d %f %d"%(var, i, i)) - Throws error because of type mismatch 

print("Welcome", "to", "Python ", "Programming", "!!!", sep= "-")
print("Welcome", "to", "Python ", "Programming", "!!!", sep= " ")#BY Default sep = " "
print("Welcome", "to", "Python ", "Programming", "!!!", sep= " ", end = "!!$")

