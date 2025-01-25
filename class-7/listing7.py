# Continue Statement 
# Make the rest of the statement after the continue statement in the loop as dead code 

fact = 1 
for i in range(1,10): 
    if(i%2 == 1):
        continue
    print(f"fact= {fact} * {i}")
    fact *= i 

print("The final answer is", fact)
    

