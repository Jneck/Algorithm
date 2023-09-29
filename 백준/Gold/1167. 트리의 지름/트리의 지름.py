import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

# 방문 리스트 초기화
v_list = [-1] * (N+1)
# 인접 리스트 초기화
n_list = [[] for i in range((N+1))]
for i in range(N):
    e_list = list(map(int, input().split()))
    node1 = -1
    node2 = -1
    for j in range(len(e_list)):
        if j == 0:
            node1 = e_list[j]
        elif j == len(e_list) - 1:
            break
        elif j % 2 == 1:
            node2 = e_list[j]
        else:
            n_list[node1].append((node2, e_list[j]))

# BFS 구현
def bfs(src):
    queue = deque()
    queue.append(src)
    v_list[src] = 0
    while queue:
        cur = queue.popleft()
        for edge in n_list[cur]:
            # 방문하지 않았다면 길이 추가하고 큐에 추가
            if -1 == v_list[edge[0]]:
                v_list[edge[0]] = v_list[cur] + edge[1]
                queue.append(edge[0])

bfs(1)
max_idx = v_list.index(max(v_list))

v_list = [-1] * (N+1)
bfs(max_idx)

print(max(v_list))