N, M = map(int, input().split())

from collections import deque

def bfs(start, visited):
    queue = deque([start])
    visited[start] = 0
    while visited[M] == -1:
        v = queue.popleft()
        for i in [v-1, v+1, 2*v]:
            if 0 <= i <= 100000:        
                if visited[i] == -1:
                    queue.append(i)
                    visited[i] = visited[v]+1
    print(visited[M])

visited = [-1] * 100001
bfs(N, visited)