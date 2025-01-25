# Sum of first n Natural Numbers using While Loop 
n = int(input("Enter the value for n? "))

sum = 0 
i = n # Loop Control Variable 
#Bottom Up Approach: n + (n-1) + (n-2) + ... 
# Top Down Approach: 1 + 2 + .. + (n-1) + (n) 
while(i >= 1 ): # Loop Condition 
    sum += i 
    i -= 1 # Loop Variable Increment or Decrement 
    print(f"Sum at {n-i}th Iteration is {sum}")

print("The Sum is", sum)
