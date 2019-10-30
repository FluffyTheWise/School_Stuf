import numpy as np

def arrange(A):
    length = np.ma.size(A)
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
        i = i +1

