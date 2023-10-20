T = int(input())

D = [[0 for i in range(15)] for i in range(15)]

for i in range(15):
    D[0][i] = i

# 호수 초기화
for i in range(1, 15):
    for j in range(1, 15):
        sum_d = 0
        for k in range(1, j+1):
            sum_d += D[i-1][k]
        D[i][j] = sum_d

for i in range(T):
    h = int(input())
    loc = int(input())
    print(D[h][loc])
