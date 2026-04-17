nums = sorted(list(map(int, input().split())))

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcd(a, b):
    return (a*b)//gcd(a, b)

print(gcd(nums[0], nums[1]))
print(lcd(nums[0], nums[1]))