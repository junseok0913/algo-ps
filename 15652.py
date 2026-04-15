from collections import defaultdict

N, M = map(int, input().split())
numbers = [n for n in range(1, N+1)]
graph = defaultdict(list)

for i in range(N):
    graph[i+1] = numbers[i:]

def dfs(cur, path):
    if len(path) == M:
        print(*path)
        path.pop()
        return
    for nxt in graph[cur]:
        path.append(nxt)
        dfs(nxt, path)
    path.pop()

for i in range(1, N+1):
    dfs(i, [i])

