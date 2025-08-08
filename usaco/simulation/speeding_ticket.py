# https://usaco.org/index.php?page=viewproblem2&cpid=568
# before 2020 => file IO!
import sys
from collections import defaultdict

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

def rl():
    return(map(int, input().split()))

n, m = rl()

road_stats = []
driving_stats = []

for i in range(n):
    length, limit = rl()
    road_stats.append((length, limit))

for i in range(m):
    length, speed = rl()
    driving_stats.append((length, speed))

driven_end = 0
max_over = 0
for (length, speed) in driving_stats:
    driven_start = driven_end
    driven_end += length

    road_end = 0
    for (ll, limit) in road_stats:
        road_start = road_end
        road_end += ll

        if driven_start < road_end and driven_end > road_start:
            max_over = max(max_over, speed-limit)
            # continue
print(max_over)