import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())

def merge_sort_A(s, e):
    # 같을 경우 그냥 반환
    if s >= e: return

    wall = (s + e) // 2 + 1
    # 각각의 분할 그룹에 대해 정렬 먼저
    merge_sort_A(s, wall-1)
    merge_sort_A(wall, e)

    # 임시리스트에 복붙
    for i in range(s, e + 1):
        tmp_list[i] = A[i]

    # 선언 및 정렬
    idx1 = s
    idx2 = wall
    idx = s

    while idx1 < wall and idx2 <= e:
        if tmp_list[idx1] < tmp_list[idx2]:
            A[idx] = tmp_list[idx1]
            idx1 += 1
            idx += 1
        else:
            A[idx] = tmp_list[idx2]
            idx2 += 1
            idx += 1

    while idx1 < wall:
        A[idx] = tmp_list[idx1]
        idx1 += 1
        idx += 1
    while idx2 <= e:
        A[idx] = tmp_list[idx2]
        idx2 += 1
        idx += 1

A = [0] * N
tmp_list = [0] * N
for i in range(N):
    A[i] = int(input())

merge_sort_A(0,N-1)

for i in range(N):
    print(str(A[i]) + '\n')