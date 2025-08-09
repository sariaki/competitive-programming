# https://open.kattis.com/problems/4thought
import sys

def rl():
    return(map(int,input().split()))

m = int(input())
ops = ['*', '+', '-', '//']

# IDEA: since we only have 4 possible ops to use 3 times (and the nrs are given), we can precompute all 4^3 permutations
sols = {}
for a in ops:
    for b in ops:
        for c in ops:
            s = '4 ' + a + ' 4 ' + b + ' 4 ' + c + ' 4'
            val = eval(s)
            s += " = " + str(val)
            sols[val] = s.replace('//', '/')

for _ in range(m):
    n = int(input())

    if n in sols:
        print(sols[n])
    else: print("no solution")