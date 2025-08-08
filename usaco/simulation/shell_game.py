# https://usaco.org/index.php?page=viewproblem2&cpid=891
# before 2020 => file IO!
import sys
from collections import defaultdict

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

def rl():
    return(map(int, input().split()))

N = int(input())

input_list = []
for i in range(N):
    a, b, g = rl()
    input_list.append([a, b, g])

global_max = 0
for i in range(1, 4):
    # assume corr pebble is i
    p = [1, 2, 3]
    nr_correct = 0

    for j in range(N):
        a, b, g = input_list[j]

        temp = p[a-1]
        p[a-1] = p[b-1]
        p[b-1] = temp

        if p[g-1] == i:
            nr_correct += 1

    if nr_correct > global_max:
        global_max = nr_correct

print(global_max)