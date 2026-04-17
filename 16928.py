from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(int)
for _ in range(N+M):
    a, b = map(int, input().split())
    graph[a] = b

cnt = 0
queue = deque([(1, 0)])
visited = set([1])
while queue:
    cur, cnt = queue.popleft()
    if cur == 100:
        print(cnt)
        break
    for dice in range(1, 7):
        nxt = cur + dice
        if nxt not in visited:
            if graph[nxt]:
                nxt = graph[nxt]
            visited.add(nxt)
            queue.append((nxt, cnt+1))