def search(nums, target: int) -> int:
    l, r = 0, len(nums)-1
    if r == 0:
        if nums[r] == target:
            return r
        else:
            return -1
    while True:
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        if nums[l] > target and nums[l-1] < target:
            return -1
        if l == r-1:
            return -1
        if nums[l] < target:
            l = (l+r) // 2
        elif nums[l] > target:
            l -= 1
    return -1

print(search([-1,5,9,12], 5))
# print(search([-1,0,3,5,9,12], 2))
# print(search([5], -5))
    
def search(self, nums, target: int) -> int:
    low_p, high_p = 0, len(nums)-1
    while low_p <= high_p:
      mid = (low_p + high_p) // 2

      if nums[mid] == target:
        return mid
      
      if nums[mid] > target:
        high_p = mid - 1
      else:
        low_p = mid + 1
    return -1