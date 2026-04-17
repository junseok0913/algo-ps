'''
# 시간초과

from collections import deque

def func_R(queue):
    new_queue = deque()
    for _ in range(len(queue)):
        n = queue.pop()
        new_queue.append(n)
    return new_queue

def func_D(queue):
    queue.popleft()
    return queue

T = int(input())
for _ in range(T):
    func = list(input())
    n = int(input())
    s = input().strip('[]')
    if s:
        queue = deque(map(int, s.split(',')))
    else:
        queue = deque()

    for cmd in func:
        if cmd == 'R':
            queue = func_R(queue)
        elif cmd == 'D':
            if queue:
                queue = func_D(queue)
            else:
                print('error')
                break
        else:
            raise NameError('Unknow func')
    
    else: # if queue: 쓰면 연산 다 완료하고 빈 배열일 때 출력 안됨
        ans = '['
        for n in queue:
            if ans == '[':
                ans = ans + str(n)
            else:
                ans = ans + ',' + str(n)
        print(ans+']')
'''

from collections import deque

T = int(input())
for _ in range(T):
    func = list(input())
    n = int(input())
    s = input().strip('[]')
    if s:
        queue = deque(map(int, s.split(',')))
    else:
        queue = deque()

    toggle = 1 # 1: ->, 0: <-

    for cmd in func:
        if cmd == 'R':
            toggle ^= 1
        elif cmd == 'D':
            if queue:
                if toggle == 1:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print('error')
                break
        else:
            raise NameError('Unknow func')

    else:
        if toggle == 0:
            new_queue = deque()
            for _ in range(len(queue)):
                n = queue.pop()
                new_queue.append(n)
            queue = new_queue
        ans = '['
        for n in queue:
            if ans == '[':
                ans = ans + str(n)
            else:
                ans = ans + ',' + str(n)
        print(ans+']')