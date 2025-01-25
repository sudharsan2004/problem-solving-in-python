#Fibonacci Sequence 
# 1 , 1, 2, 3, 5, 8, ....
def fib(n):
    if(n == 0 ):
        return 0
    elif(n == 1):
        return 1 
    else: 
        return fib(n-2) + fib(n-1)


n = int(input("Enter the Number?"))
for i in range(1,n+1):
    print(fib(i), end= "\t")