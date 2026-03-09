num = int(input())

for i in range(num):
    string = list(input())
    score, cnt = 0, 0
    for j in range(len(string)):
        if string[j] == 'O':
            cnt += 1
            score = score+cnt
        else:
            cnt = 0
    print(score)