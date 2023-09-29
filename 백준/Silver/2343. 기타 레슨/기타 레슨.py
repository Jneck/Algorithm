import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 블루레이가 될 수 있는 최소 크기(마지막 원소의 크기)부터 최대 크기까지(한번에 다 넣는 크기)
start = max(A)
end = sum(A)
m = 0
while start < end:
    m = (start + end) // 2
    cnt_m = 0
    sum_lesson = 0
    for lesson in A:
        sum_lesson += lesson
        if sum_lesson > m:
            sum_lesson = lesson
            cnt_m += 1
    cnt_m += 1
    # m에 더해지는 값이 다른 이유
    # 주어진 블루레이보다 많이 담기면 무조건 그 값도 안되는 값
    # 주어진 블루레이보다 적게 담기면
    if cnt_m < M:
        end = m -1
    elif cnt_m == M:
        end = m
    else:
        start = m + 1

print((start + end) // 2)
