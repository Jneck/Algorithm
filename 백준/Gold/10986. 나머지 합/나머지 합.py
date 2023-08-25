import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum_remainder_list = [0] * N
sum_remainder_list[0] = num_list[0]
for i in range(1, len(num_list)):
    sum_remainder_list[i] = (num_list[i]+sum_remainder_list[i-1]) % M
# Ai ~ Aj까지의 합이라는 뜻은 sum[j]-sum[i-1]
answer_list = [0] * M
answer = 0
for i in range(N):
    remainder = sum_remainder_list[i] % M
    if remainder == 0:
        answer += 1         # 처음부터 다 더했을때 애초에 나머지 0인 경우
    answer_list[remainder] += 1     # 구간합을 구했을 때 나머지가 같은 케이스를 셈

for i in range(M):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if answer_list[i] > 1:      # 나머지 같은 게 두개 이상이라면
        answer += (answer_list[i] * (answer_list[i] - 1) // 2)      # 두가지를 뽑는 경우의 수 조합 -> n*n-1//2*1
print(answer)
