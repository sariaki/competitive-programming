def findMin(nums) -> int:
    l, r = 0, len(nums)-1

    if r <= 3:
        return min(nums)
    if nums[0] > nums[1]:
        return nums[1]
    _min = 5001

    while l < r:
        m = (l+r)//2

        if nums[m] < _min:
            _min = nums[m]

        if nums[l] < nums[r]:
            r = m-1
        else:
            l = m+1

        # if l == r-1:
        #     return min(nums[l], nums[r])
    return _min

print(findMin([3,4,5,1,2]))
print(findMin([1,2,3,4,5]))
#[5,1,2,3,4]
print(findMin([5,6,1,2,3,4]))
#[7,8,1,2,3,4,5,6]
print(findMin([7,8,1,2,3,4,5,6]))
print(findMin([2,3,4,5,1]))
