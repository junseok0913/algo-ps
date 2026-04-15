'''
더 짧고 쉽게 백트래킹으로 풀 수 있음
'''

from collections import defaultdict

N, M = map(int, input().split())
numbers = [n for n in range(1, N+1)]
graph = defaultdict(list)

for i in range(N):
    graph[i+1] = numbers[i+1:]

path = []
def dfs(cur, path):
    path.append(cur)
    if len(path) == M:
        print(*path)
        path.pop()
        return
    for nxt in graph[cur]:
        dfs(nxt, path)
    path.pop()

for i in range(1, N+1):
    dfs(i, [])