from collections import defaultdict

computer = int(input())
net = int(input())

graph = defaultdict(list)

for _ in range(net):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
def dfs(node, visited):
    for nxt in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            dfs(nxt, visited)
visited.add(1)
dfs(1, visited)
print(len(visited)-1)