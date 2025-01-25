#Fibonacci Sequence using Memoisation 
# 1 , 1, 2, 3, 5, 8, ....
d = {0:0, 1:1} # Global Variable 
def fib(n):
    if(n in d.keys()):
        return d[n]
    else: 
        t = fib(n-2) + fib(n-1)
        d[n] = t # Populate the Dictionary 
        return t 


n = int(input("Enter the Number?"))
for i in range(1,n+1):
    print(fib(i), end= "\t")