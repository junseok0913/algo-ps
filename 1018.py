N, M = map(int, input().split())
chess = []
for _ in range(N):
    chess.append(list(input()))

if N < 8 or M < 8:
    raise ValueError

ans = 64
start_W = list('WBWBWBWB')
start_B = list('BWBWBWBW')

for n in range(N-8+1):
    for m in range(M-8+1):
        board = [row[m:m+8] for row in chess[n:n+8]]

        # Case: WB...
        i = 1
        cnt_w = 0
        for row in board:
            if i%2 == 1:
                cnt_w += sum(a != b for a, b in zip(row, start_B))
            else:
                cnt_w += sum(a != b for a, b in zip(row, start_W))
            i+=1
        
        # Case: BW...
        j = 1
        cnt_b = 0
        for row in board:
            if j%2 == 1:
                cnt_b += sum(a != b for a, b in zip(row, start_W))
            else:
                cnt_b += sum(a != b for a, b in zip(row, start_B))
            j+=1
        
        if min(cnt_w, cnt_b) < ans:
            ans = min(cnt_w, cnt_b)

print(ans)
