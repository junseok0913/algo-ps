from collections import deque

N, M = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input())))

queue = deque([(0, 0, False, 1)])
visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True

while queue:
    a, b, wall, cnt = queue.popleft()
    if a == N-1 and b == M-1:
        print(cnt)
        break
    for nxt_a, nxt_b in [[a+1, b], [a-1, b], [a, b+1], [a,b-1]]:
        if 0 <= nxt_a < N and 0<= nxt_b < M:
            if matrix[nxt_a][nxt_b] == 0 and not visited[nxt_a][nxt_b][wall]:
                queue.append((nxt_a, nxt_b, wall, cnt+1))
                visited[nxt_a][nxt_b][wall] = True
            elif wall == False and matrix[nxt_a][nxt_b] == 1 and not visited[nxt_a][nxt_b][1]:
                queue.append((nxt_a, nxt_b, True, cnt+1))
                visited[nxt_a][nxt_b][1] = True
else:
    print(-1)