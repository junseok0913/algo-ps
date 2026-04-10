'''
아무 노드에서나 출발해서 가장 먼 노드를 찾으면,
그 노드는 반드시 지름의 한쪽 끝점이다.

1. 1번 노드에서 DFS -> 가장 먼 노드 찾기 (이게 지름의 한쪽 끝)
2. 그 노드에서 DFS -> 가장 먼 거리 찾기 (이게 답)
'''

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

far_node = 0
far_dist = 0
visited = set()

def dfs(node, dist, visited):
    global far_node, far_dist
    if dist > far_dist:
        far_dist = dist
        far_node = node
    for nxt, w in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            dfs(nxt, dist+w , visited)

visited.add(1)
dfs(1, 0, visited)
start = far_node

far_node = 0
far_dist = 0
visited = set()

visited.add(start)
dfs(start, 0, visited)
print(far_dist)