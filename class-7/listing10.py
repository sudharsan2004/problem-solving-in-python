# Pattern Problems 
# Left Upper Triangle Pattern 
"""
Input: 2
Output: 
**
*

Input: 3 
Output: 
***
**
*
"""

n = int(input("Enter the value for n: "))
i = n
for row in range(0,n): 
    for column in range(row, n):
        print(i, end="")
    print("") # Next Line
    i -= 1 
