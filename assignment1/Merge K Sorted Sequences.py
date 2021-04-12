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