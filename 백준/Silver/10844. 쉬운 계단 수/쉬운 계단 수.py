N = int(input())
# 안쪽 배열의 0번 인덱스: 마지막 자리 0인 경우
# 안쪽 배열의 1번 인덱스: 마지막 자리 1인 경우 ....
mod = 10**9

DP = [[1 for i in range(10)] for i in range(N+1)]
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i - 1][1]
        elif j == 9:
            DP[i][j] = DP[i - 1][8]
        else:
            DP[i][j] = (DP[i-1][j-1] + DP[i-1][j+1]) % mod

answer = 0
for value in DP[N][1:]:
    answer = (answer + value) % mod
print(answer)