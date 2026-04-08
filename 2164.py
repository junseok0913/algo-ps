from collections import deque

N = int(input())
queue = deque(i for i in range(N, 0, -1))

trash = True
while len(queue)>1:
    if trash:
        queue.pop()
        trash = False
    else:
        temp = queue.pop()
        queue.appendleft(temp)
        trash = True

print(queue[0])