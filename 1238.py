from collections import defaultdict
import heapq

INF = int(1e9)

N, M, X = map(int, input().split())
graph = defaultdict(list)
rev_graph = defaultdict(list)

for _ in range(M):
    start, end, d = map(int, input().split())
    graph[start].append([end, d])
    rev_graph[end].append((start, d))

def dijkstra(graph, start):
    dist = [INF] * (N+1)
    dist[start] = 0
    hq = [[start, 0]]
    while hq:
        cur, d = heapq.heappop(hq)

        if d > dist[cur]:
            continue
        
        for nxt, nxt_d in graph[cur]:
            nxt_dist = d + nxt_d
            if nxt_dist < dist[nxt]:
                dist[nxt] = nxt_dist
                heapq.heappush(hq, [nxt, nxt_dist])
    return dist

go = dijkstra(rev_graph, X)
back = dijkstra(graph, X)

print(max(go[i] + back[i] for i in range(1, N+1)))