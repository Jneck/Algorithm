N = int(input())

DP1 = [1 for i in range(N)]     # 1을 선택했을 때 뒤에 남은 자릿수(인덱스)별 가짓수
DP0 = [1 for i in range(N)]     # 0을 선택했을 때 뒤에 남은 자릿수(인덱스)별 가짓수

for i in range(1, N):
    DP0[i] = DP0[i-1] + DP1[i-1]    # 다음으로 올 수 있는게 0 또는 1
    DP1[i] = DP0[i-1]               # 다음이 무조건 0이 되므로

print(DP1[N-1])