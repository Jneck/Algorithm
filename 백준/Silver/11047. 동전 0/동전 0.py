import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for i in range(N)]

idx = N-1
answer= 0
while K > 0:
    if K >= A[idx]:
        answer += K // A[idx]
        K = K % A[idx]
    idx -= 1

print(answer)