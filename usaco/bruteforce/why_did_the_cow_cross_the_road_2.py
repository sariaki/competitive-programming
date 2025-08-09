# https://usaco.org/index.php?page=viewproblem2&cpid=712
import sys
from collections import defaultdict, deque

sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

def rl():
    return(map(int,input().split()))

cows = input()

# IDEA 1 (fails on > test 3): every cow after current cow needs to exit before current cow 
# => stack
# O(n)

# crossings = []
# for c in cows:
#     if len(crossings) > 0 and c == crossings[-1]:
#         crossings.pop()
#         continue

#     crossings.append(c)

# print(set(crossings))
# print(len(set(crossings)) // 2)

# IDEA 2: iterate over all possible pairs to see if they cross
# O(n^4)
count = 0
for i, a in enumerate(cows):
    end = cows.rfind(a)

    for j in range(i+1, end):
        b = cows[j]
        end2 = cows.rfind(b)

        if end2 > end:
            count += 1
print(count)