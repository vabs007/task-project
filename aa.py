def rightRotateByOne(A):
 
    last = A[-1]
    for i in reversed(range(len(A) - 1)):
        A[i + 1] = A[i]
 
    A[0] = last
 
 

def rightRotate(A, k):
 
 
    if k < 0 or k >= len(A):
        return
 
    for i in range(k):
        rightRotateByOne(A)
 
 
if __name__ == '__main__':
 
    A = [-1,-100,3,99]
    k = 2
 
    rightRotate(A, k)
    print(A)



        
