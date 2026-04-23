from collections import defaultdict

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
graph = defaultdict(list)
for _ in range(V):
    lst = list(map(int, input().split()))
    for i in range(1, len(lst), 2):
        if lst[i] == -1:
            break
        graph[lst[0]].append([lst[i], lst[i+1]])

visited = set()
ans = []
def dfs(node, dist):
    if len(visited) <= V:
        for nxt, nxt_dist in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                ans.append([nxt, dist+nxt_dist])
                dfs(nxt, dist+nxt_dist)

visited.add(1)
dfs(1, 0)
first = sorted(ans, key = lambda x : x[1], reverse=True)[0]

visited = set()
visited.add(first[0])
ans = []
dfs(first[0], 0)
second = sorted(ans, key = lambda x: x[1], reverse=True)[0]
print(second[1])
