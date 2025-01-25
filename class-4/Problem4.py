lst = []
for i in range(0,5):
    lst.append(int(input(f"Enter the {i+1} Mark")))

lst.sort(reverse = True)
print("%d is the Highest Mark"%lst[0]) 