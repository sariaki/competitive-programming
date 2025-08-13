# https://usaco.org/index.php?page=viewproblem2&cpid=1037
from collections import defaultdict
import sys

sys.setrecursionlimit(5000)

sys.stdin = open("tracing.in", "r")
sys.stdout = open("tracing.out", "w")

input = lambda: sys.stdin.readline().strip()

def print(value):
    sys.stdout.write(str(value) + '\n')

def rl():
    return map(int,input().split())

# UNFINISHED

n, t = rl()
curr_state = input()
times = []
xs = []
ys = []
for _ in range(t):
    time, x, y = rl()
    times.append(time)
    xs.append(x)
    ys.append(y)

# get possible candidates for patient 0
# IDEA: Since N and T are so heavily constrained, we could iterate all cows and simulate the infection process for each cow
for i in range(1, n+1):
    # assume cow i is patient 0
    infected = defaultdict(int)
    infected[i] = 1
    for j in range(t):
        if xs[j] == infected.keys():
            # other cow is infected
            infected[ys[j]] = 1
        elif ys[j] == infected.keys():
            infected[xs[j]] = 1
    