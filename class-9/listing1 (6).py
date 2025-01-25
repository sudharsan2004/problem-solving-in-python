# Importing sys Package 
import sys

# Finding Number of Arguments 
n = len(sys.argv)

# Since the first argument is file name, from second argument 
n = len(sys.argv) - 1 
l = list(sys.argv[1:])

# To Convert the input to integer 
l = [int(i) for i in sys.argv[1:]]
print(l)

d = {0:1, 1:1 }
# Factorial Function 
def fact(n):
    if n in d.keys(): 
        return d[n] 
    else: 
        f = fact(n-1) * n 
        d[n] = f 
        return f 
    
for i in l: 
    print(fact(i))

print(d)