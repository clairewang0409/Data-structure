def getMax(operations):
    # Write your code here
    #print(operations)
     
    maxarr = []
    final = []
    
    for i in operations:
        if i == "2":
            if len(maxarr) > 0:
                maxarr.pop()

        elif i == "3":
            if len(maxarr) > 0:
                print(maxarr[-1])
                final.append(maxarr[-1])

        else:
            x = int(i[2:])
            if len(maxarr) == 0:
                maxarr.append(x)
            else:
                currMax = maxarr[-1]
                maxarr.append(x if x > currMax else currMax)
            
    return final