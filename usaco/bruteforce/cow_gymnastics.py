# https://usaco.org/index.php?page=viewproblem2&cpid=963
# before 2020 => file IO!
import sys
from collections import defaultdict

sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

def rl():
    return(map(int,input().split()))

k, n = rl()

cow_pairs = []
line = list(rl())

# find combinations of ALL cows
for i in range(n):
    for j in range(i+1, n):
        cow_pairs.append((line[i], line[j]))

for _ in range(1, k):
    line = list(rl())
    combinations = defaultdict(int)

    # construct new cow pairings
    for i in range(n):
        for j in range(i+1, n):
            combinations[(line[i], line[j])] = 1

    # for each cow_pair, find it in new list; if not found: remove from cow_pairs
    for i, pair in enumerate(cow_pairs):
        if combinations[pair] != 1: # faster to not delete (O(n)) and instead just set to 0 and filter later
            cow_pairs[i] = 0

# nr. of cow pairs
nr = 0
for pair in cow_pairs:
    # print(pair)
    if pair != 0:
        nr += 1
print(nr)

# solution suboptimal
# cf. https://usaco.guide/problems/usaco-963/user-solutions