import sys
sys.setrecursionlimit(10**6)

start, target = map(int, input().split())
ans = []

def dfs(cur, cnt):
    if cur == target:
        ans.append(cnt)
        return
    if cur > target:
        return
    for nxt in [2 * cur, int(str(cur) + '1')]:
        dfs(nxt, cnt + 1)

dfs(start, 0)
print(min(ans) + 1 if ans else -1)