cnt = int(input())
members = []
for i in range(cnt):
    age, name = input().split()
    members.append([int(age), name])

members = sorted(members, key = lambda x: x[0])
for i in range(len(members)):
    print(members[i][0], members[i][1])