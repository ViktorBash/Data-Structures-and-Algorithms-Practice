"""
Google CodeJam
"""

import itertools


def compute(string):
    for perm in itertools.permutations(string):
        item = "".join(perm)
        done = True
        for i in range(len(item)):
            if item[i] == string[i]:
                done = False
        if done:
            return item
    return "IMPOSSIBLE"


t = int(input())
for a in range(1, t + 1):
    string = str(input())
    result = compute(string)
    print(f"Case #{a}: {result}")
