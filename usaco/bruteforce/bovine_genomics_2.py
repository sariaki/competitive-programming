# https://usaco.org/index.php?page=viewproblem2&cpid=739
import sys
from collections import defaultdict

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

def rl():
    return(map(int,input().split()))

n, m = rl()

spotty = []
for _ in range(n):
    spotty.append(input())

nspotty = []
for _ in range(n):
    nspotty.append(input())

# IDEA 1 (fails > 4 due to time constraints): naive bruteforce
# O(m^4*n^2)
# count = 0
# # get triple of genes
# for i in range(m):
#     for j in range(i+1, m):
#         for k in range(j+1, m):
#             unique = True
#             for l1 in range(n):
#                 for l2 in range(n):
#                     if nspotty[l2][i] == spotty[l1][i] and nspotty[l2][j] == spotty[l1][j] and nspotty[l2][k] == spotty[l1][k]:
#                         # triple does not uniquely identify spottyness
#                         unique = False
#                         break
#                 if not unique:
#                     break
#             if unique:
#                 count += 1
# print(count)

# IDEA 2: less naive bruteforce, leveraging better datastructures
# # O(m^4*2n)=O(m^4*n)
count = 0
# get triple of genes
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            unique = True
            triple_set = set()
            # check if no spotty triple == nspotty triple
            for l1 in range(n):
                triple_set.add((spotty[l1][i], spotty[l1][j], spotty[l1][k]))
            for l2 in range(n):
                if (nspotty[l2][i], nspotty[l2][j], nspotty[l2][k]) in triple_set:
                    # triple does not uniquely identify spottyness
                    unique = False
                    break
            if unique:
                count += 1
print(count)