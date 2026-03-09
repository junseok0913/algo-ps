'''
print(len(input().split())) 한 줄이면 끝남...
split()이 앞뒤 공백 제거 + 공백 기준 분리 + 빈 문자열이면 빈 리스트 반환
모두 해줌  
'''

sentence = input()
start, end, cnt = 0, 0, 0

if sentence.split() == []:
    print("0")

else:
    import re

    sentence = list(sentence)

    for i in range(len(sentence)):
        if re.match(r'[a-zA-Z]', sentence[i]):
            start = i
            break

    for i in reversed(range(len(sentence))):
        if re.match(r'[a-zA-Z]', sentence[i]):
            end = i
            break

    for i in range(start, end):
        if sentence[i] == ' ':
            cnt += 1
        
    print(cnt+1)