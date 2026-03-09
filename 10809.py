word = list(input())
hash_map = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}

for pos in reversed(range(len(word))):
    hash_map[word[pos]] = pos

print(*hash_map.values())

