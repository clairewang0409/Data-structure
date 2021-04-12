def TopKIntegerSequence(matrix):
    # Write your code here

    K = []
    A = []
    for row in matrix:
        for i in row:
            heapq.heappush(A, i)
        K.append(A[0])        
        heapq.heappop(A)
    return K