#Check whether the number is even or not 

#Users Input 
num = int(input("Enter a integer: ")) 

#If the number is divisible by 2 or in other words remainder of number / 2 is 0 then it is even or else it is not 
#Usage of if Condition 
"""
#If Statement 
if(condition / Expression):
    Action Block

#If Else statement 
if(condition / Expression): 
    Action Block (True Block)
else: 
    Action Block (False Block)

#If else if 
if (condition / Expression): 
    action block
elif(condition / Expression): 
    Action Block 
... 
else : #Else is optional one everywhere 
    Action Block  
"""
if(num % 2 == 0): #The output of the expression would be boolean (in Most cases)  
    #num % 2 --> 0 or 1 
    # Equality Operator "==" return either true or false (Boolean Variable) Boolean Values: True, False
    print(f"{num} is an Even Number")
else: 
    print("%d is an odd number"%num)
