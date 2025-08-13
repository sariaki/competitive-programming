# https://cses.fi/problemset/task/1623
from math import inf
import sys
import faulthandler
faulthandler.enable()

sys.setrecursionlimit(900000000)
input = lambda: sys.stdin.readline().strip()

def print(value):
    sys.stdout.write(str(value) + '\n')

def rl():
    return map(int,input().split())

n = int(input())

ps = list(rl())

# PROBLEM: Create 2 groups of apples s.t. min weight diff is min
# IDEA (too slow!): just check all permutations
# O(n!*n); Darren Yao's book recommends n <= 10 for O(n!)
# def permutations(ps, begin):
#     if begin == n:
#         print("hi")
#         return [[]]
    
#     perms = permutations(ps, begin+1)
#     new_perms = []
#     for perm in perms:
#         for i in range(len(perm)+1):
#             newp = []
#             for j, p in enumerate(perm):
#                 if i == j:
#                     newp.append(ps[begin])

#                 newp.append(p)
#             if i == len(perm):
#                 newp.append(ps[begin])
#             new_perms.append(newp)
#     return new_perms

# perms = permutations(ps_, 0)
# min_diff = 10000000
# for p in perms:
#     for sep in range(n):
#         s1 = sum(p[:sep])
#         s2 = sum(p[sep:])
#         min_diff = min(abs(s1-s2), min_diff)
# print(min_diff)

# IDEA: Since the weights are just added, we don't actually care about *all* permutations and skip the ones that contain the same elements
# => we care about subsets
# O(2^n)
def solve(begin, s1, s2):
    if begin == n:
        return abs(s1-s2)

    a = solve(begin+1, s1+ps[begin], s2)
    b = solve(begin+1, s1, s2+ps[begin])
    m = min(a, b)
    return m

print(solve(0, 0, 0))