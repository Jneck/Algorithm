import sys
import math
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())

n_list = [[]for i in range(N+1)]
v_list = [False for i in range(N+1)]
# 인접 리스트로 트리 구현
for i in range(1, N):
    s, e = map(int, input().split())
    n_list[s].append(e)
    n_list[e].append(s)

d_list = [0 for i in range(N+1)]
k = 0
while 2**k <= N:
    k += 1

P = [[0 for i in range(N+1)] for i in range(k+1)]

# 탐색하며 tree data 세팅
def dfs_and_set(cur_node):
    for new_node in n_list[cur_node]:
        if not v_list[new_node]:
            v_list[new_node] = True
            d_list[new_node] = 1 + d_list[cur_node]
            P[0][new_node] = cur_node
            dfs_and_set(new_node)

d_list[1] = 0
v_list[1] = True
dfs_and_set(1)

# 점화식을 이용하여 값 채우기
for i in range(1, k+1): #  k값
    for j in range(1, N+1):
        P[i][j] = P[i-1][P[i-1][j]]

def LCA_fast(a, b):
    if d_list[a] > d_list[b]:
        temp = a
        a = b
        b = temp

    # 높이 맞추기 낮은 것부터 -> 크게
    if d_list[a] < d_list[b]:
        for k_idx in range(k, -1, -1):
            # 만약에 depth차가 이동할 거리보다 ㅋ면
            if 2**k_idx <= d_list[b] - d_list[a]:
                b = P[k_idx][b]

    # 최소 공통 조상 찾기
    for k_idx in range(k, -1, -1):
        # 다를 때 저장하고 break
        if P[k_idx][a] != P[k_idx][b]:
            a = P[k_idx][a]
            b = P[k_idx][b]
    # 달라졌을 때 같다면
    if a != b:
        return P[0][a]
    else:
        return a

M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    print(str(LCA_fast(a, b)) + '\n')
