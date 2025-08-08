
def generate(numRows: int):
    if numRows == 1:
        return [1]
    elif numRows == 2:
        return [1, 1]
    
    l = []
    for i in range(numRows):
        l.append([1])

        if i == 0:
            continue
        if i != 1:
            for j in range(len(l[i-1])-1):
                s = l[i-1][j] + l[i-1][j+1]
                l[i].append(s)
        
        l[i].append(1)
    return l

print(generate(5))