# Insertion Sort for Ascending Order

def InsertionSort(A): 
    for i in range(1, len(A)): # Second Element to last Element
        key = A[i]
        j = i - 1
        while(j >= 0 and A[j] > key): 
            A[j+1] = A[j] 
            j = j - 1 
        A[j+1] = key 
    return A

print(InsertionSort([5,4,3,2,1]))

