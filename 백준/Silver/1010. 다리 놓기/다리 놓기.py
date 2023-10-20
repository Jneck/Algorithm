T = int(input())

P = [[0 for i in range(30)]for i in range(30)]

for i in range(30):
    P[i][i] = 1
    P[i][1] = i
    P[i][0] = 1

for i in range(3, 30):
    for j in range(2, 30):
        P[i][j] = P[i-1][j] + P[i-1][j-1]

for i in range(T):
    N, M = map(int, input().split())
    print(P[M][N])