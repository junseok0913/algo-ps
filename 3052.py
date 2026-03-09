num_list = []
for i in range(10):
    num_list.append(int(input()))

ans = set()
for num in num_list:
    ans.add(num%42)

print(len(ans))

