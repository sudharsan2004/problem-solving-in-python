# Sum of first n Natural Numbers using While Loop - Top Down Approach 
n = int(input("Enter the value for n? "))
sum = 0 
i = 1 # Loop Control Variable 
#Bottom Up Approach: n + (n-1) + (n-2) + ... 
# Top Down Approach: 1 + 2 + .. + (n-1) + (n) 
while(i <= n ): # Loop Condition 
    sum += i 
    print(f"Sum at {i}th Iteration is {sum}")
    i += 1 # Loop Variable Increment or Decrement 

print("The Sum is", sum)