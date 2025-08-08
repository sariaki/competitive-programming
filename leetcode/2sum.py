from collections import defaultdict

def twoSum(nums, target: int):
    d = defaultdict(list)
    for i in range(len(nums)):
        if len(d[target-nums[i]]) > 0:
            return [d[target-nums[i]][0], i]

        d[nums[i]].append(i)


a = [2,7,11,15]
print(twoSum(a, 9))