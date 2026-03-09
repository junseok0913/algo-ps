case_cnt = int(input())
case = []
for i in range(case_cnt):
    case.append(list(map(int, input().split())))

res = []
for h,w,n in case:
    floor = h if n%h==0 else n%h
    room = n//h if n%h==0 else n//h+1
    if room < 10:
        print(str(floor)+'0'+str(room))
    else:
        print(str(floor)+''+str(room))