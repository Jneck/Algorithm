N, K =map(int,input().split())
D = [[1 for i in range(N+1)]for i in range(N+1)]

# 리스트 초기화
for i in range(1, N+1):
    D[i][1] = i
    D[i][i] = 1
    D[i][0] = 1

for i in range(3, N+1):
    for j in range(2, i):
        D[i][j] = (D[i-1][j] + D[i-1][j-1]) % 10007

print(D[N][K])