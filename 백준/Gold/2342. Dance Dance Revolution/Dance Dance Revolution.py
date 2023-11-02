import sys
input = sys.stdin.readline
input_list = list(map(int, input().split()))
DP = [[[sys.maxsize for i in range(5)]for j in range(5)]for k in range(len(input_list))] # [N까지 수행 후][왼발 현재 위치][오른발 현재 위치]의 최솟값

# 어디서 어디로 이동할 때 드는 비용
MP = [[0, 2, 2, 2, 2],
      [2,1,3,4,3],
      [2,3,1,3,4],
      [2,4,3,1,3],
      [2,3,4,3,1]]


DP[0][0][input_list[0]] = MP[0][input_list[0]]# 오른발 움직였을 때
DP[0][input_list[0]][0] = MP[0][input_list[0]]  # 왼발 움직였을 때

for i in range(1, len(input_list)-1):
    for l in range(5):          # 왼발 경우의 수
        if l == input_list[i]:  # 두 발이 같은 지점에 있으면 안됨.
            continue
        for r in range(5):      # 모든 오른발 경우의 수에 대해 현재 값으로 오는 경우
            DP[i][l][input_list[i]] = min(DP[i-1][l][r] + MP[r][input_list[i]], DP[i][l][input_list[i]])

    for r in range(5):
        if r == input_list[i]:  # 두 발이 같은 지점에 있으면 안됨.
            continue
        for l in range(5):      # 모든 왼발 경우의 수에 대해 현재 값으로 오는 경우
            DP[i][input_list[i]][r] = min(DP[i-1][l][r] + MP[l][input_list[i]], DP[i][input_list[i]][r])

result = sys.maxsize
for i in range(5):
    for j in range(5):
        result = min(result, DP[len(input_list)-2][i][j])

print(result)