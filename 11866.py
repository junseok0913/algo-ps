N, K = map(int, input().split())

lst = list(range(1, N+1))
ans = []

cur = K-1
while len(lst) > 0:
    ans.append(lst.pop(cur))
    cur += (K-1)
    if cur >= len(lst) and len(lst) > 0:
        cur = cur%len(lst)

print('<'+', '.join(map(str, ans))+'>')