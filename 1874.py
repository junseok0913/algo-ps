'''
재귀 쓰지 맙시다.
판별 로직도 틀렸습니다.
n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
    if num_list[-1] == n:
        check = i

check_list = num_list[check:]
if check_list != sorted(check_list, reverse=True):
    print("NO")
else:
    init_list = list(range(1, n+1))
    stack = []
    cur = 0

    def pop_all(cur):
        if len(stack) > 0 and cur < n and stack[-1] == num_list[cur]:
            stack.pop()
            print('-')
            cur += 1
            return pop_all(cur)
        else:
            return cur

    for num in init_list:
        stack.append(num)
        print('+')
        cur = pop_all(cur)
'''

n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

stack = []
res = []
for num in range(1,n+1):
    stack.append(num)
    res.append('+')
    while len(stack) > 0 and stack[-1] == num_list[0]:
        stack.pop()
        num_list.pop(0)
        res.append('-')

if len(stack) > 0:
    print('NO')
else:
    for char in res:
        print(char)