'''
from itertools import permutations

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
ans = sorted(set(permutations(numbers, M)))

for ns in ans:
    print(*ns)
'''

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))
path = []
visited = [False] * N

def dfs(path):
    if len(path) == M:
        print(*path)
        return
    prev = -1

    for i in range(N):
        if visited[i] == True or numbers[i] == prev:
            continue
        prev = numbers[i]
        path.append(numbers[i])
        visited[i] = True
        dfs(path)
        path.pop()
        visited[i] = False

dfs(list())
