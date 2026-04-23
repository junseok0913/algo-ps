from collections import deque
n, m = map(int, input().split())
grid = list()
target = (-1, -1)

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    if 2 in row:
        target = (i, row.index(2))

ans = [[-1]*m for _ in range(n)]
ans[target[0]][target[1]] = 0
queue = deque([(target[0], target[1])])
while queue:
    r, c = queue.popleft()
    for nxt_r, nxt_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if 0 <= nxt_r < n and 0 <= nxt_c < m:
            if grid[nxt_r][nxt_c] != 0 and ans[nxt_r][nxt_c] == -1:
                ans[nxt_r][nxt_c] = ans[r][c] + 1
                queue.append((nxt_r, nxt_c))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            ans[i][j] = 0
    print(*ans[i])