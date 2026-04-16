from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited = set([1])
ans = list(-1 for _ in range(N-1))
while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(nxt)
            ans[nxt-2] = cur

for prev in ans:
    print(prev)