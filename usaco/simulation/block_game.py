# https://usaco.org/index.php?page=viewproblem2&cpid=664
# before 2020 => file IO!
import sys
from collections import defaultdict
from string import ascii_lowercase

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

def rl():
    return map(int, input().split())

# "irrespective of which face OF EACH board is showing, the cows can spell all N visible words"

n = int(input())

letters = defaultdict(int)

# SUBOPTIMAL
# for _ in range(n):
#     w1, w2 = map(str, input().split())

#     for c in w1:
#         letters[c] += 1

#         if c in w2:
#             w2 = w2.replace(c, "", 1) # DON'T replace all occurences. Ex: if we have multiple 'a's in the second word, and only 1 'a' in the first, we still need 2 blocks

#     for c in w2:
#         letters[c] += 1

# OPTIMAL
for _ in range(n):
    w1, w2 = map(str, input().split())

    local_count1 = defaultdict(int)
    for c in w1:
        letters[c] += 1
        local_count1[c] += 1

    local_count2 = defaultdict(int)
    for c in w2:
        local_count2[c] += 1
        if local_count2[c] > local_count1[c]:
            letters[c] += 1

for c in ascii_lowercase:
    print(letters[c])