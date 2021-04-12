def MergeKSortedSequences(sequences):
    # Write your code here
    arr = []
    for i in sequences:
        for j in i:
            arr.append(j)
    arr.sort()
    arr.reverse()
    #print(arr)
    return arr



'''
def MergeTwoSortedList(ListA, ListB):
    """
    A simple function that merges two sorted lists(increase) into one sorted list(increase)
    ListA and ListB must be a sorted list !!!
    """
    MergeList = []
    i = 0
    j = 0
    while( i < len(ListA) and j < len(ListB)):
        if ListA[i] < ListB[j]:
            MergeList.append(ListA[i])
            i += 1
        else:
            MergeList.append(ListB[j])
            j += 1
            
    if i < len(ListA):
        MergeList.extend(ListA[i:])
        
    if j < len(ListB):
        MergeList.extend(ListB[j:])

    return(MergeList)
'''
