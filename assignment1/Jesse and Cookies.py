def cookies(k, A):
    #
    # Write your code here.
    #
   
    heapq.heapify(A)
    t = 0
    
    if A[0] < k and len(A) < 2 :
        return -1
        
    else:     
        while A[0] < k and len(A) > 1:
            t += 1
            s1 = heapq.heappop(A)
            s2 = heapq.heappop(A)
            mix = s1 + (s2*2)
            heapq.heappush(A, mix)
        if A[0] < k:
            return -1
        else:
            return t
    
    '''
    heapq.heapify(A)
    res = 0
    if sum(A) >= k:
        while A[0] < k and res <= n:
            res += 1
            temp1 = heapq.heappop(A)
            temp2 = heapq.heappop(A)
            heapq.heappush(A, temp1 + 2 * temp2)
        return (res if res <= n else -1)
    else:
        return -1
    '''