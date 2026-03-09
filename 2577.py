'''
a, b, c = [int(input()) for _ in range(3)]                                    
res = str(a * b * c)                                                          
for i in range(10):                                                           
    print(res.count(str(i)))
'''

num = []
for i in range(3):
    num.append(int(input()))

res = list(str(num[0] * num[1] * num[2]))
count = [0]*10

for n in res:
    count[int(n)] += 1

for cnt in count:
    print(cnt)