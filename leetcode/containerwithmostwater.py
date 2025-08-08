
def maxArea(height) -> int:
    l, r = 0, len(height)-1
    res = 0
    while l < r:
        s = (r-l) * min(height[r], height[l]) # To not slant the container
        if s > res:
            res = s
        
        if height[r] < height[l]:
            r -= 1
            continue
        elif height[l] < height[r]:
            l += 1
            continue

        r -= 1
        l += 1

    return res

print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([1,1]))