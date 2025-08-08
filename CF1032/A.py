import sys

input = lambda: sys.stdin.readline().strip()

def print(value):
    sys.stdout.write(str(value) + '\n')

def rl():
    return(map(int,input().split()))

def solve(): #
    n, s = rl()
    ints = list(rl())

    a = abs(s-min(ints))
    b = abs(s-max(ints))
    x=0
    if a < b:
        x = a
    else:
        x = b
    
    x += abs(max(ints)-min(ints))
    print(x)


t = int(input())
for i in range(t):
    solve()