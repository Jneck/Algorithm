import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
find_A = list(map(int, input().split()))

def bs_A(target_num, s, e):
    while s <= e:
        m = (s + e) // 2
        if A[m] == target_num:
            return m
        # 데이터 셋 선택
        if A[m] < target_num:
            s = m+1
        else:
            e = m-1
    return -1

for num in find_A:
    if -1 == bs_A(num, 0, N-1):
        print('0\n')
    else:
        print('1\n')