'''
기가 막힌 아이디어
'''

N = int(input())
M = int(input())
S = input()
answer = 0
cnt = 0
i = 0

while i < M - 1:
    if S[i] == 'I' and S[i+1] == 'O':
        cnt += 1
        if cnt >= N:
            if S[i + 2] == 'I':
                answer += 1
        i += 2
    else:
        cnt = 0
        i += 1

print(answer)