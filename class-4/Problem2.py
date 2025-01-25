#Find the minimum of three numbers 
a = int(input("Enter Value for a: "))
b = int(input("Enter Value for b: "))
c = int(input("Enter Value for c: "))

#Case   -- Condition 
#a is greater -- a > b and a > c 
#b is greater -- b > a and b > c 
#c is greater -- c > a and c > b 

if((a > b) and (a > c)): # True and True --> Then only expression which is true 
    print(f"{a} is Greater.")
elif((b > a) and (b > c)): 
    print(f"{b} is Greater.")
else: 
    print(f"{c} is greater.")
