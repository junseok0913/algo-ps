N = int(input())
vps_list = []
for i in range(N):
    vps_list.append(list(input()))

for vps_s in vps_list:
    check = []
    for vps in vps_s:
        if vps == '(':
            check.append('(')
        elif vps == ')' and len(check) > 0:
            check.pop()
        else:
            check = [-1]
            break
    if len(check) != 0:
        print('NO')
    else:
        print('YES')