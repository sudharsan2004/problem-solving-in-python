#Beta Function Implementation 

n = int(input("Enter a value for n: "))
m = int(input("Enter a value for m: "))
result = 1 

# Numerator : (m-1)! 
for i in range(m-1, 1, -1): # Starts with m-1 and ends at 2 
    result *= i 

# Numerator : (n-1)! 
for i in range(n-1, 1, -1):
    result *= i 

#Denominator 
for i in range(m+n-1, 1, -1): 
    result /= i 

print(f"Result is {result}")