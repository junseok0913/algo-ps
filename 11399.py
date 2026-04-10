N = int(input())
times = sorted(map(int, list(input().split())))
ans = 0
for i in range(len(times)):
    temp = sum(times[:i+1])
    ans+=temp
print(ans)