n = int(input())
meeting_list = []
for i in range(n):
    meeting_list.append(list(map(int, input().split())))

meeting_list.sort(key=lambda x : (x[1], x[0]))
ans = list([meeting_list.pop(0)])
for start, end in meeting_list:
    if start >= ans[-1][1]:
        ans.append([start, end])
    else:
        continue

print(len(ans))