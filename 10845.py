from collections import deque

n = int(input())
cmd_list = []
for i in range(n):
    cmd_list.append(list(input().split()))

dq = deque()
for cmd in cmd_list:
    if cmd[0] == 'push':
        dq.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif cmd[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    elif cmd[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    else:
        raise Exception('Unknown Command')
        