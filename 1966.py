'''
deque랑 tuple로 별도 index 리스트 없애고 pop(0) 대신 popleft() 사용
'''
cnt = int(input())

case_list = []
for i in range(cnt):
    N, M = map(int, input().split())
    case_list.append([[N, M], list(map(int, input().split()))])

for [n, target], case in case_list:
    ans = 0
    index = [0]*n
    index[target] = 1
    while len(case) > 0:
        if case[0] == max(case):
            case.pop(0)
            index.pop(0)
            ans += 1
            if sum(index) < 1:
                break
        else:
            case.append(case[0])
            index.append(index[0])
            case.pop(0)
            index.pop(0)
    print(ans)