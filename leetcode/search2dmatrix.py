# O(log2(m*n))
def searchMatrix(matrix, target: int) -> bool:
    l, r = 0, len(matrix)-1

    if r == 0 and len(matrix[0])-1 == 0: 
        if matrix[0][0] == target:
            return True
        else: 
            return False

    while l <= r:
        sum1 = (l + r) // 2
    
        if matrix[sum1][0] < target and matrix[sum1][len(matrix[sum1])-1] > target:
            l2, r2 = 0, len(matrix[sum1])-1

            while l2 <= r2:
                sum2 = (l2+r2) // 2
                if matrix[sum1][sum2] == target:
                    return True
                
                if matrix[sum1][sum2] > target:
                     r2 = sum2-1
                elif matrix[sum1][sum2] < target:
                     l2 = sum2+1
            return False
        elif matrix[sum1][len(matrix[sum1])-1] == target:
            return True
        elif matrix[sum1][0] == target:
            return True
        else:
            if matrix[sum1][len(matrix[sum1])-1] > target:
                r = sum1-1
            elif matrix[sum1][len(matrix[sum1])-1] < target:
                l = sum1+1
    return False

# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(searchMatrix([[1, 2]], 2))