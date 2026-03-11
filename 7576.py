import sys
input = sys.stdin.readline

from collections import deque

Y, X = map(int, input().split())
graph = []
starts = []
for i in range(X):
    graph.append(list(map(int, input().split())))
    for j in range(Y):
        if graph[-1][j] == 1:
            starts.append([i, j])

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def bfs(graph, starts):
    queue = deque(starts)
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx <= X-1 and 0 <= ny <= Y-1 and graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

bfs(graph, starts)
ans = max(max(row) for row in graph)-1

if any(0 in row for row in graph):
    print(-1)
else:
    print(ans)