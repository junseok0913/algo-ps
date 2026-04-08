N = int(input())
A = set(map(int, input().split()))
M = int(input())
checklist = list(map(int, input().split()))

for num in checklist:
    if num in A:
        print(1)
    else:
        print(0)