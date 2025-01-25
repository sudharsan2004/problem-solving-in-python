m = int(input("Enter m:"))
n = int(input("Enter n:"))

r1 = r2 =r3 = 1 
for i in range(m-1, 1, -2):
    r1 *= i 

for i in range(n-1, 1, -2):
    r2 *= i 

for i in range(m+n, 1, -2):
    r3 *= i 

result = (r1 * r2)/ r3 
if((m%2 == 0) and (n%2 == 0)):
    result *= 1.57 

print("Result:", result )

p = m - 1
q = n - 1
result = 1 
for i in range(m+n, 1, -2):
    if(p>=2): 
        result *= p 
        p -= 2
    if(q >= 2):
        result *= q 
        q -= 2 
    result /= i 

if((m%2 == 0) and (n%2 == 0)):
    result *= 1.57 

print(f"The result is {result}")
