cnt = int(input())
cood_list = []
for i in range(cnt):
    cood_list.append(list(map(int, input().split())))

for x, y in sorted(cood_list):
    print(x, y)