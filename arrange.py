import numpy as np

def arrange(A):
    length = np.size(A)
    x = 0
    i = 0
    temp = 0
    
    while True:
        if x == length:
            return A
        if i == length - 1:
            i = 0
        if A[i] > A[i + 1]:
            temp = A[i + 1] 
            A[i + 1] = A[i]
            A[i] = temp
            x = 0
        else:
            x = x + 1
        i = i + 1

def ndarrange(A):
    dim = np.size(A,0)
    
    for i in range (dim):
        A[i] = arrange(A[i])
    return A

def axisarrange(A, B):
    length = np.size(A)
    x = 0
    i = 0
    temp = 0
    temp2 = 0
    
    while True:
        if x == length:
            return A, B
        if i == length - 1:
            i = 0
        if A[i] > A[i + 1]:
            temp = A[i + 1]
            temp2 = B[i + 1]
            A[i + 1] = A[i]
            B[i + 1] = B[i]
            A[i] = temp
            B[i] = temp2
            x = 0
        else:
            x = x + 1
        i = i + 1
        
def arrangeback(A):
    A = np.flip(arrange(A))
    return A

def ndarrangeback(A):
    dim = np.size(A,0)
    
    for i in range (dim):
        A[i] = arrangeback(A[i])
    return A
    