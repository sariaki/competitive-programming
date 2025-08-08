# https://codeforces.com/gym/102951/problem/A
import sys
from collections import defaultdict
from math import *

def rl():
    return(map(int,input().split()))

n = int(input())

xs = list(rl())
ys = list(rl())

m = 0
for i in range(n):
    xi = xs[i]
    yi = ys[i]

    for j in range(i+1, n): # skip previous combinations (we've already explored them). skip self since distance will always be 0
        xj = xs[j]
        yj = ys[j]

        m = max(m, (xi-xj) ** 2 + (yi - yj) ** 2)
print(m)