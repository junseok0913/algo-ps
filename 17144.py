from collections import deque

R, C, T = map(int, input().split())
home = list()
cleaner = []

for r in range(R):
    row = list(map(int, input().split()))
    if row[0] == -1:
        cleaner.append([r, 0])
    home.append(row)

def spread(home):
    add_home = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if home[i][j] > 0:
                for a, b in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                    if 0 <= a <= R-1 and 0 <= b <= C-1:
                        if home[a][b] != -1:
                            add_home[i][j] = add_home[i][j] - home[i][j]//5
                            add_home[a][b] = add_home[a][b] + home[i][j]//5
    return [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(home, add_home)]

def clean():
    r1, r2 = cleaner[0][0], cleaner[1][0]

    for i in range(r1-1, 0, -1):
        home[i][0] = home[i-1][0]
    for j in range(0, C-1):
        home[0][j] = home[0][j+1]
    for i in range(0, r1):
        home[i][C-1] = home[i+1][C-1]
    for j in range(C-1, 1, -1):
        home[r1][j] = home[r1][j-1]
    home[r1][1] = 0

    for i in range(r2+1, R-1):
        home[i][0] = home[i+1][0]
    for j in range(0, C-1):
        home[R-1][j] = home[R-1][j+1]
    for i in range(R-1, r2, -1):
        home[i][C-1] = home[i-1][C-1]
    for j in range(C-1, 1, -1):
        home[r2][j] = home[r2][j-1]
    home[r2][1] = 0
        

for _ in range(T):
    home = spread(home)
    clean()

print(sum(sum(row) for row in home)+2)