N, M = map(int, input().split())
N_s, M_s = set(), set()

for i in range(N):
    N_s.add(input())
for j in range(M):
    M_s.add(input())

ans = sorted(list(N_s & M_s))
print(len(ans))
for name in ans:
    print(name)