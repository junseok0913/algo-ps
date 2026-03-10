cases = []
while True:
    cases.append(sorted(list(map(int, input().split())), reverse=True))
    if cases[-1] == [0,0,0]:
        cases.pop()
        break

for a, b, c in cases:
    if a**2 == b**2+c**2:
        print('right')
    else:
        print('wrong')