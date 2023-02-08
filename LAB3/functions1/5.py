from itertools import permutations
def strPermutations(str):
    allperm = permutations(str)
    for x in allperm:
        print(*x)

strPermutations(input())