# https://usaco.org/index.php?page=viewproblem2&cpid=736
import sys
from collections import defaultdict

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

def rl():
    return(map(int,input().split()))

n, m = rl()

spotty_genomes = [[None for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(m):
        spotty_genomes[i][j] = line[j]

nspotty_genomes = [[None for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(m):
        nspotty_genomes[i][j] = line[j]

# IDEA: if a spotty genome contains a char from the nspotty genomes then it can't be used for prediction!
good_count = 0
for i in range(m):
    good = True
    for j in range(n):
        genome = spotty_genomes[j][i]

        # check if genome i occurs for nspotty
        for k in range(n):
            if nspotty_genomes[k][i] == genome:
                good = False
                break # genome does not uniquely identify spottyness
        if good == False:
            break
    if good:
        good_count += 1

print(good_count)

# solution suboptimal
# cf. https://usaco.guide/problems/usaco-736-bovine-genomics/solution