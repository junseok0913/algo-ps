import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
visited = set()
stack = list()

def dfs(begin):
    stack.append(begin)
    visited.add(begin)
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)

for i in range(1, N+1):
    if i not in visited:
        dfs(i)
        ans += 1

print(ans)