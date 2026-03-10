'''
cmd_list로 한번에 입력 받으면 메모리 초과
'''
n = int(input())
S = set()
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == 'add':
        if cmd[1] not in S:
            S.add(cmd[1])
    elif cmd[0] == 'remove':
        if cmd[1] in S:
            S.remove(cmd[1])
    elif cmd[0] == 'check':
        if cmd[1] in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if cmd[1] in S:
            S.remove(cmd[1])
        else:
            S.add(cmd[1])
    elif cmd[0] == 'all':
        S = set(map(str, range(1,21)))
    elif cmd[0] == 'empty':
        S = set()
    else:
        raise Exception('Unknown Command')