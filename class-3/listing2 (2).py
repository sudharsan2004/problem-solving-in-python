#Sum of first n Natural Numbers 

#How to get the users' input? 
#input Function 
# var = input("Quote")
# type(var) --> String 
n = int(input("Enter the Number n: "))
sum = 0
loop_control = 0 
for i in range(1,n+1):
    prev_sum = sum 
    sum = sum + i
    loop_control += 1 #loop_control = loop_control + 1
    print("Iteration %d: i = %d\n\tsum = %d + %d = %d\n"%(loop_control, i, prev_sum, i, sum))
          
"""
For Example, last input n = 4 
range(1,5) --> [1,2,3,4]
Iteration 1: i = 1 
    sum = 0 + 1 = 1 

Iteration 2: i = 2 
    sum = 1 + 2 = 3 

Iteration 3: i = 3 
    sum = 3 + 3 = 6 

Iteration 4: i = 4 
    sum = 6 + 4 = 10 
"""

print(f"Sum of first {n} Natrual Numbers is", sum)

