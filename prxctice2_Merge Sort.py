def mergesort(A):
    if len(A)>1:   
        mid = len(A)//2
        L = A[ : mid]
        R = A[mid : ]
        
        mergesort(L)
        mergesort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
                
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1            



def MergeSortInNondecreasingOrder(A):
    # Write your code here
    de_buffer = A[:]
    mergesort(de_buffer)
    return(de_buffer)

def MergeSortInNonincreasingOrder(A):
    # Write your code here
    de_buffer = A[:]
    mergesort(de_buffer)
    de_buffer.reverse()
    return(de_buffer)
