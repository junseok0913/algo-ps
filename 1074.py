N, R, C = map(int, input().split())

def update(n, r, c, ans):
    
    def z(n, r, c):
        half = 2**(n-1)
        if r < half:
            if c < half:
                return 0
            else:
                return 1
        else:
            if c < half:
                return 2
            else:
                return 3

    z = z(n, r, c)
    ans += (2**(n-1))*(2**(n-1))*z
    if z == 3:
        return r-2**(n-1), c-2**(n-1), ans
    elif z == 2:
        return r-2**(n-1), c, ans
    elif z == 1:
        return r, c-2**(n-1), ans
    else:
        return r, c, ans
    

ans = 0
for n in range(N, 0, -1):
    R, C, ans = update(n, R, C, ans)
print(ans)