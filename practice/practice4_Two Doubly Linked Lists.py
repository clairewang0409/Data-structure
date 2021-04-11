def PerformOperationsOnLists(operations):
    # Write your code here
    L = [[], []]
    
    for x, id1, pos1, id2, pos2 in operations:
        if x == 0:
            L[id1].insert(pos1,id2)

        elif x == 1:
            del L[id1][pos1]  
            
        else:
            P1 = L[id2][pos2:] 
            L[id2] = L[id2][:pos2]
            L[id1] = L[id1][:pos1] + P1 + L[id1][pos1:]

    return L[0] + L[1]
            