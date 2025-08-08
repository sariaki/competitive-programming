# https://usaco.org/index.php?page=viewproblem2&cpid=855
# before 2020 => file IO!
import sys
from collections import defaultdict

sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

def rl():
    return(map(int, input().split()))

buckets = []
for _ in range(3):
    c, m = rl()
    buckets.append([m, c]) # capacity, milk

for i in range(100):
    b_idx1 = i % 3
    b_idx2 = (b_idx1 + 1) % 3
    # print((b_idx1, b_idx2))

    amount = buckets[b_idx2][1] - buckets[b_idx2][0] # max - current

    if buckets[b_idx1][0] >= amount: # we have more than we need: we must fill to the max
        buckets[b_idx2][0] = buckets[b_idx2][1]
        buckets[b_idx1][0] -= amount
    else: # we can safely fill everything into the bucket
        buckets[b_idx2][0] += buckets[b_idx1][0]
        buckets[b_idx1][0] = 0
        
print(buckets[0][0])
print(buckets[1][0])
print(buckets[2][0])