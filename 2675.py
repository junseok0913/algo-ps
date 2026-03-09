num = int(input())
case = []
for i in range(num):
    case.append(list(input().split()))

for R, S in case:
    ans = []
    for char in list(S):
        if char == '\\':
            ans.append(str('\\'*int(R)))
        else:
            ans.append(str(char*int(R)))
    print("".join(ans))