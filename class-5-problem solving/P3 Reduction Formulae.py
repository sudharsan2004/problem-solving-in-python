# Reduction Formulae 
n = int(input("Enter the value for n: "))
result = 1 
#Numerator 
for i in range(n-1, 1,-2): 
    result *= i 

#Denominator 
for j in range(n, 1, -2):
    result /= j

# % --> Remainder Operator 
# 5 % 2 --> 1 
# 9 % 5 --> 4 
if(n%2 == 0): 
    result *= (3.14/2)

print(f"Result is {result}") 

