N, M = map(int, input().split())
card_list = list(map(int, input().split()))

from itertools import combinations

choice = list(combinations(card_list, 3))

res = 0
diff = M
for abc in choice:
    if M - sum(abc) >= 0:
        if diff > M - sum(abc):
            diff = M - sum(abc)
            res = sum(abc)

print(res)