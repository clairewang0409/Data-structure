def equalStacks(h1, h2, h3):
    # Write your code here
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    while not (sum1 == sum2 == sum3):
        mx = max(sum1, sum2, sum3)
        if (sum1 == mx):
            sum1 -= h1[0]
            h1.pop(0)
        if (sum2 == mx):
            sum2 -= h2[0]
            h2.pop(0)
        if (sum3 == mx):
            sum3 -= h3[0]
            h3.pop(0)
            
    return sum1