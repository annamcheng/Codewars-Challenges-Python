def oddNum(l,r):
    result = []
    [result.append(num) for num in range(l,r+1) if num&1]
    return result
print(oddNum(2,5))
