num = int(input())

for i in range(1, num+1):
    if num-i>0:
        print(" "*(num-i-1), "*"*i)
    else:
        print("*"*i)
