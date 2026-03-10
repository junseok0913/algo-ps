'''
cmd_list로 한번에 입력 받으면 메모리 초과
set 아닌 비트 마스크
'''
import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
S = 0
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'add':
        S |= (1 << int(cmd[1]))
    elif cmd[0] == 'remove':
        S &= ~(1 << int(cmd[1]))
    elif cmd[0] == 'check':
        if S & (1 << int(cmd[1])):
            write('1\n')
        else:
            write('0\n')
    elif cmd[0] == 'toggle':
        S ^= (1 << int(cmd[1]))
    elif cmd[0] == 'all':
        S = (1 << 21) - 2
    elif cmd[0] == 'empty':
        S = 0
    else:
        raise Exception('Unknown Command')