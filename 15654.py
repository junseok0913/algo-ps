from itertools import permutations

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

if len(numbers) != N:
    raise ValueError

comb = list(permutations(numbers, M))
for s in comb:
    print(*s)
