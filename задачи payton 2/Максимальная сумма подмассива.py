def m(a):
    sum1 = 0  
    sum2 = 0  
    for num in a:
        sum2 += num  
        if sum2 < 0:
            sum2 = 0  
        sum1 = max(sum1, sum2)
    return sum1
result = m([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)  
