# https://cses.fi/problemset/task/1622
from collections import defaultdict
import sys
import faulthandler
faulthandler.enable()

sys.setrecursionlimit(900000000)
input = lambda: sys.stdin.readline().strip()

def print(value):
    sys.stdout.write(str(value) + '\n')

def rl():
    return map(int,input().split())

# Given a string, construct all possible permutations
inp = input()
n = len(inp)
# IDEA 1 (works): Since n < 8 <= 10, we can naively do a complete search
# NOTE: This is implemented suboptimally
# O(n!*n) because of str.replace()
# perms = set()
# def permutations(new, possibilities):
#     if new in perms:
#         return

#     if len(possibilities) == 0:
#         perms.add(new)
#         return

#     for i, c in enumerate(possibilities):
#         permutations(new+c, possibilities[:i]+possibilities[i+1:])

# permutations("", inp)
# print(len(perms))
# for p in sorted(perms):
#     print(p)

# IDEA 2: to get rid of the n-factor: instead of actively removing elements from a string (O(n)), use a better datastructure, the hashmap, to remove them in constant time
# O(n!)
perms = []
# def permutations(new, u):
#     if len(new) == n:
#         perms.append(new)
#         return
    
#     for k in u.keys():
#         if u[k] > 0:
#             u2 = u.copy()
#             u2[k] -= 1
#             permutations(new+k, u2)

used = defaultdict(int)

# instead of always creating a new hashmap, we can just backtrack
def permutations(new):
    if len(new) == n:
        perms.append(new)
        return
    
    for k in used.keys():
        if used[k] > 0:
            used[k] -= 1
            permutations(new+k)
            used[k] += 1

for c in inp:
    used[c] += 1
permutations("")
print(len(perms))
for p in sorted(perms):
    print(p)