import heapq

def HeapSort(A):
    output = []
    heapq.heapify(A)
    while len(A) > 0:
        output.append(heapq.heappop(A))
    return(output)



def HeapSortInNondecreasingOrder(A):
    # Write your code here
    nd_heap = A[:]
    sorted_nd_heap = HeapSort(nd_heap)
    return(sorted_nd_heap)
