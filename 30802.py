N = int(input())
by_size = list(map(int, input().split()))
T, P = map(int, input().split())

t = list(map(lambda x: x//T if x%T == 0 else x//T + 1, by_size))
print(sum(t))
print(N//P, N%P)