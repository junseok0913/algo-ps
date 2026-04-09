from collections import defaultdict, deque

case = int(input())
for i in range(case):
    M, N, K = map(int, input().split())
    baechu = set()
    graph = defaultdict(list)
    for j in range(K):
        m, n = map(int, input().split())
        baechu.add((m, n))
    
    visited = set()
    ans = 0
    for cur in baechu:
        if cur not in visited:
            queue = deque([cur])
            visited.add(cur)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x+dx, y+dy
                    if (nx, ny) in baechu and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            ans += 1
    print(ans)
