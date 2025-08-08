import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

def print(value):
    sys.stdout.write(str(value) + '\n')

def rl():
    return(map(int,input().split()))

def solve(): #
    n, m = rl()

    l = []
    mm1 = 0
    count = 0
    mi = 0
    # find row and collumn with max INDIVIDUAL value
    for i in range(n):
        x = list(rl())
        l.append(x)
        s = max(x)
        if s > mm1 or (s == mm1 and x.count(s) > count):
            mm1 = s
            mi = i
            count = x.count(s)
    
    for i in range(m):
        l[mi][i] -= 1

    mm2 = 0
    mj = 0
    count = 0
    for i in range(m):
        lc = 0
        for j in range(n):
            s = l[j][i]
            if s > mm2 or (s == mm2 and lc > count):
                mj = i
                mm2 = s
                lc += 1

    for i in range(n):
        l[i][mj] -= 1

    mm = 0
    for i in range(n):
        m = max(l[i])
        if m > mm:
            mm = m
    print(mm)

t = int(input())
for i in range(t):
    solve()