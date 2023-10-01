import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

s = 1
e = k

# log2 k만큼
while s < e:
    m = (s+e)//2
    sum_cnt = 0
    # N만큼
    for i in range(1, N+1):
        sum_cnt += min(m//i, N)
    if sum_cnt <= k-1:
        s = m+1
    else:
        e = m

print(s)