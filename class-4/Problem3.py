#Optimizing the Problem 2 
"""
if((a > b) and (a > c)): # True and True --> Then only expression which is true 
    print(f"{a} is Greater.")
elif((b > a) and (b > c)): 
    print(f"{b} is Greater.")
else: 
    print(f"{c} is greater.")
"""
#Find the minimum of three numbers 
a = int(input("Enter Value for a: "))
b = int(input("Enter Value for b: "))
c = int(input("Enter Value for c: "))

if(a > b):
    #a is greater than b 
    if(a > c):
        print("%d is the greater value"%a)
    else: #when c is greater than a 
        print("%d is the greater value"%c)
else: #b is greater 
    if(b > c): 
        print(f"{b} is greater value")
    else: 
        print("%d is the greater value"%c)


#Test Case: What are all the variety of input that can be given? 
#Test Case 1: 11, 25, 10 
#Test Case 2: 9, 10, 25
#Test Case 3: 25, 0, 10