import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

def print(value):
    sys.stdout.write(str(value) + '\n')

def rl():
    return(map(int,input().split()))

def repetitions(x):
    reps = defaultdict(list)
    for i, char in enumerate(x): 
       reps[char].append(i)
    return reps

def solve(): #
    n = int(input())
    s = str(input())
    # does a character repeat between idx 0 and n? 
    # EX: [a a b c] => a="a", c="b c" => b="a"
    # EX: [a b b c] => a="a b", c = "c" => b="b"
    # if yes => A=yes
    reps = repetitions(s)
    for rep in reps.values():
        if len(rep) > 1:
            for r in rep:
                if r != n-1 and r != 0:
                    print("Yes")
                    return
    print("No")



t = int(input())
for i in range(t):
    solve()