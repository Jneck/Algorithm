import sys
input = sys.stdin.readline
print = sys.stdout.write

from collections import deque

bfs_deque = deque()
N, M ,V = map(int,input().split())
n_list = [[] for i in range(N+1)]
v_list = [False] * (N+1)

def dfs(src):
    print(str(src) + ' ')

    for new_src in n_list[src]:
        if not v_list[new_src]:
            v_list[new_src] = True
            dfs(new_src)

# 간선 설정
for i in range(M):
    node1, node2 = map(int, input().split())
    n_list[node1].append(node2)
    n_list[node2].append(node1)

# 작은 것부터 방문할 수 있게 sorting
for i in range(1, N+1):
    n_list[i].sort()

# dfs는 재귀 함수로 구현
v_list[V] = True
dfs(V)
print('\n')

# 방문 리스트 초기화
for i in range(N+1):
    v_list[i] = False

# bfs는 큐에 값없을때까지 반복
v_list[V] = True
bfs_deque.append(V)
while bfs_deque:
    src = bfs_deque.popleft()
    print(str(src) + ' ')

    # 다음 방문지들 방문
    for new_src in n_list[src]:
        if not v_list[new_src]:
            v_list[new_src] = True
            bfs_deque.append(new_src)
