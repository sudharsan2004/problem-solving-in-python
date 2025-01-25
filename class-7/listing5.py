# Infinte Loop
# Condition is always true.... --> Executes the loop for infinite 
# 1. Loop Condition ==> range(0,n)
# 2. Loop Body ==> Action Block
# 3. Increment or Decrement ; Obvious in While Loop 
i = 1 
j = 1
while True:
    while True: 
        print("Welcome to Infinite Loop!! ", i, end="")
        if(i == 10):
            break
        i += 1 
    print("Outerloop")
    j += 1 
    if(j == 3): 
        break
    
# Ctrl + c ==> Keyboard Import 