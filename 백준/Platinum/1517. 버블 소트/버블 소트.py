import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
tmp_arr = [0] * N

answer = 0

def merge_sort_A(s, e):
    global answer
    if s >= e:
        return
    m = (s+e)//2
    merge_sort_A(s, m)
    merge_sort_A(m+1, e)

    for i in range(s, e+1):
        tmp_arr[i] = A[i]

    idx1 = s
    idx2 = m+1
    idx = s

    # 두 그룹이 아직 모두 남아있을때
    while (idx1 <= m) and (idx2 <= e):
        if tmp_arr[idx1] <= tmp_arr[idx2]:
            A[idx] = tmp_arr[idx1]
            idx1 += 1
        else:
            A[idx] = tmp_arr[idx2]
            answer += (idx2 - idx)
            idx2 += 1
        idx += 1

    # 두 그룹중 한개가 떨어졌을 때 나머지 처리
    while idx1 <= m:
        A[idx] = tmp_arr[idx1]
        idx1 += 1
        idx += 1
    while idx2 <= e:
        A[idx] = tmp_arr[idx2]
        answer += (idx2 - idx)
        idx2 += 1
        idx += 1


merge_sort_A(0, N-1)
print(answer)