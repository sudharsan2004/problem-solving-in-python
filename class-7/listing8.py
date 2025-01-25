# Pattern Problems 
# Square Pattern 
"""
Input: 2
Output: 
**
**

Input: 3 
Output: 
***
***
*** 
"""

n = int(input("Enter the value for n: "))
for row in range(0,n): 
    for column in range(0, n):
        print("*", end="")
    print("") # Next Line 
