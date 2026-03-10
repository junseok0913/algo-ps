import sys
input = sys.stdin.readline

N = int(input())
card_list = list(input().split())
M = int(input())
target_list = list(input().split())

from collections import Counter 
counter = Counter(card_list)
ans = []
'''
for target in target_list:
    if target in card_list: <- 리스트 탐색 O(n) 시간초과 N*M 
        ans.append(counter[target])
    else:
        ans.append('0')
'''
for target in target_list:
    ans.append(counter[target])

print(*ans)
