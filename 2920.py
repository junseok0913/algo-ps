music = list(map(int, input().split()))

if music == list(range(1,9)):
    print("ascending")
elif music == list(reversed(range(1,9))):
    print("descending")
else:
    print("mixed")
