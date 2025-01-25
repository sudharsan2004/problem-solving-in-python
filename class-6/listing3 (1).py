#Matrix Multiplication
# Matrix Element 
m = int(input("Enter the value of A: "))
n = int(input("Enter the value of B: "))
A = []
if(m <= 0 or n <= 0 ):
	exit() # Program ends here 

for i in range(0,m): 
    l = [] # consists only one row 
    for j in range(0,n): 
        k = int(input(f"Enter the value of A[{i}][{j}]"))
        l.append(k)
    A.append(l)

#A = [[1, 0 , 0], [0,1,0], [0,0,1]]
p = int(input("Enter the value of A: "))
q = int(input("Enter the value of B: "))
B = []
if(p <= 0 or q <= 0 ):
	exit()
elif(p != n): #Matrix Multiplication Condition 
	print("Multipication is invalid") 

for i in range(0,p): 
    l = [] 
    for j in range(0,q): 
        k = int(input(f"Enter the value of A[{i}][{j}]"))
        l.append(k)
    B.append(l)		
		
C = [] 
for i in range(0,m): # c [i][j] # Rows 
	l = [] 
	for j in range(0,q): #c[i][j] # Columns 
		t = 0 
		for k in range(0,n):  #Traversal # Individual Element 
			t += A[i][k] * B[k][j] 
		l.append(t)
	C.append(l)

print(C)
