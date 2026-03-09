cnt = int(input())
word_set = set()
for i in range(cnt):
    word_set.add(input())

res = sorted(list(word_set), key=lambda x: (len(x), x))
for i in res:
    print(i)