import math
N = int(input())
nums = list(map(int, input().split()))

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

cnt = 0
for n in nums:
    if is_prime(n) == True:
        cnt+=1
print(cnt)