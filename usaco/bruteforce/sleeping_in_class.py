# https://usaco.org/index.php?page=viewproblem2&cpid=1203
import sys

sys.setrecursionlimit(5000)
input = lambda: sys.stdin.readline().strip()

def print(value):
    sys.stdout.write(str(value) + '\n')

def rl():
    return map(int,input().split())

t = int(input())

# IDEA 1 (fails for testS > 1): go through all possible permutations of adjacent combinations. first one to reach goal is outputted
# O(n!) ...yea this sucks.
def get_combinations_naive(state, count): # make sure that state is in the form [[x, x, x, ...]]
    states = []
    for s in state:
        # check
        bad = False
        for j in range(len(s)-1):
            if s[j] != s[j+1]:
                bad = True
        if not bad:
            # print(s)
            return count

        for j in range(len(s)-1):
            x = [s[j]+s[j+1]]
            x += (s[j+2:])
            x = s[:j] + x
            
            states.append(x)
    return get_combinations_naive(states, count + 1)

# IDEA 2 (see image): iterate possible divisors of sum(a). these are possible numbers which the array will be constructed out of. if it is possible to do so, we've found our sol
# 
def get_combinations(a):
    s = sum(a)

    for i in range(1, s+1):
        if not (s % i == 0):
            continue
        elm_count = s / i

        # check if elm == i is constructable
        constructable = True
        state_sum = 0
        for elm in a:
            state_sum += elm
            if state_sum == i:
                state_sum = 0
            elif state_sum > i:
                constructable = False
                break

        if constructable:
            steps = int(len(a)-elm_count)
            return steps

for _ in range(t):
    n = int(input())
    a = list(rl())

    x = get_combinations(a)
    if x == None:
        print(0)
    else: print(x)