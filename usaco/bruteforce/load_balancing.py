# https://usaco.org/index.php?page=viewproblem2&cpid=617
from math import inf
import sys
from collections import defaultdict, deque

sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

def rl():
    return(map(int,input().split()))

N, B = rl()

xs = []
ys = []
possible_a = []
possible_b = []
for new_a in range(N):
    x, y = rl()
    xs.append(x)
    ys.append(y)
    # IDEA 3: 
    # (1): len(xs) could be way smaller than [0, B]
    # (2): xs and ys could have giant jumps in them => incrementing a or b here slowly does not accomplish anything
    possible_a.append(x-1) # + or minus does not matter here
    possible_b.append(y-1)

# IDEA 3: optimize (a, b) combinations to be smaller
a = 0
b = 0
M = inf
for new_a in possible_a:
    for new_b in possible_b:
        # compute m for each field & get minimum:
        m1 = 0
        m2 = 0
        m3 = 0
        m4 = 0
        for k in range(N):
            if xs[k] > new_a and ys[k] > new_b:
                m1 += 1
            if xs[k] < new_a and ys[k] > new_b:
                m2 += 1
            if xs[k] < new_a and ys[k] < new_b:
                m3 += 1
            if xs[k] > new_a and ys[k] < new_b:
                m4 += 1
        # print(m1, m2, m3, m4)
        local_max = max(m1, m2, m3, m4)
        # print(local_max)
        M = min(M, local_max)
print(M)

# IDEA 1 (fails for test > 6): iterate through all possible combinations of (a, b) [even nrs] s.t. argmin(M)
# => works, but we need to optimize
# O(a*b*N)
# a = 0
# b = 0
# M = inf
# for new_a in range(0, B, 2):
#     for new_b in range(0, B, 2):
#         # compute m for each field & get minimum:
        
#         m1 = 0
#         m2 = 0
#         m3 = 0
#         m4 = 0
#         for k in range(N):
#             if xs[k] > new_a and ys[k] > new_b:
#                 m1 += 1
#             if xs[k] < new_a and ys[k] > new_b:
#                 m2 += 1
#             if xs[k] < new_a and ys[k] < new_b:
#                 m3 += 1
#             if xs[k] > new_a and ys[k] < new_b:
#                 m4 += 1
#         # print(m1, m2, m3, m4)
#         local_max = max(m1, m2, m3, m4)
#         # print(local_max)
#         M = min(M, local_max)
# print(M)

# IDEA 2:
# okay this idea is horrible and leads to no real improvement
# a = 0
# b = 0
# M = inf
# for new_a in range(0, B, 2):
#     gea = []
#     lea = []
#     start_ge = 0
#     begin_ge = True
#     start_le = 0
#     begin_le = True
#     for i in range(N):
#         if xs[i] > new_a:
#             if begin_ge:
#                 begin_ge = False
#                 start_ge = i
#             gea.append(i)
#         if xs[i] < new_a:
#             if begin_le:
#                 begin_le = False
#                 start_le = i
#             lea.append(i)
#     for new_b in range(0, B, 2):
#         m1, m2, m3, m4 = 0, 0, 0, 0
#         for i in gea[start_ge+1:]:
#             if ys[i] > new_b:
#                 m1 += 1
#             if ys[i] < new_b:
#                 m2 += 1
#         for i in lea[start_le+1:]:
#             if ys[i] > new_b:
#                 m3 += 1
#             if ys[i] < new_b:
#                 m4 += 1
#         # print(m1, m2, m3, m4)
#         local_max = max(m1, m2, m3, m4)
#         # print(local_max)
#         M = min(M, local_max)
# print(M)