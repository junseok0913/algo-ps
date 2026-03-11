'''
use pypy3
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    start, target = map(int, input().split())
    
    prev = [-1] * 10000
    cmd = [''] * 10000
    prev[start] = start
    queue = deque([start])
    
    while prev[target] == -1:
        cur = queue.popleft()
        d = (2 * cur) % 10000
        s = cur - 1 if cur else 9999
        l = (cur % 1000) * 10 + cur // 1000
        r = (cur % 10) * 1000 + cur // 10
        if prev[d] == -1:
            prev[d] = cur; cmd[d] = 'D'; queue.append(d)
        if prev[s] == -1:
            prev[s] = cur; cmd[s] = 'S'; queue.append(s)
        if prev[l] == -1:
            prev[l] = cur; cmd[l] = 'L'; queue.append(l)
        if prev[r] == -1:
            prev[r] = cur; cmd[r] = 'R'; queue.append(r)
    
    path = []
    node = target
    while node != start:
        path.append(cmd[node])
        node = prev[node]
    path.reverse()
    sys.stdout.write(''.join(path) + '\n')