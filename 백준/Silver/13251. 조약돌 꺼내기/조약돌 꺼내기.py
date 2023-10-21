M = int(input())
color_stones = list(map(int, input().split()))
K = int(input())

D = [[0 for i in range(sum(color_stones)+1)] for i in range(sum(color_stones)+1)]

for i in range(sum(color_stones)+1):
    D[i][0] = 1
    D[i][1] = i
    D[i][i] = 1

for i in range(3, sum(color_stones)+1):
    for j in range(2, sum(color_stones)+1):
        D[i][j] = D[i-1][j] + D[i-1][j-1]

total_cnt = 0
for color in color_stones:
    total_cnt += D[color][K]

print(total_cnt / D[sum(color_stones)][K])
