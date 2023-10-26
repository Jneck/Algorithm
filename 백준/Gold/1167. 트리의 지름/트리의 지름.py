import sys

input = sys.stdin.readline
from collections import deque

N = int(input())

v_list = [-1] * (N + 1)  # 방문 리스트 초기화
n_list = [[] for i in range((N + 1))]  # 인접 리스트 초기화
for i in range(N):
    e_list = list(map(int, input().split()))
    for j in range(1, len(e_list) - 1, 2):
        n_list[e_list[0]].append((e_list[j], e_list[j + 1]))

def bfs(src):
    queue = deque()
    queue.append(src)       # 큐에 시작 노드 넣고 방문처리
    v_list[src] = 0
    while queue:            # 큐가 빌 때까지, 방문하여 관련 작업 처리
        cur = queue.popleft()
        for edge in n_list[cur]:
            # 방문하지 않았다면 길이 추가하고 큐에 추가
            # 트리이기 때문에 사이클 x -> 각 노드에 방문할 때 길이가 유일한 경로
            if -1 == v_list[edge[0]]:
                v_list[edge[0]] = v_list[cur] + edge[1]
                queue.append(edge[0])


bfs(1)
max_node = v_list.index(max(v_list))     # 첫 번째 순회 후 가장 거리가 먼 노드를 저장

v_list = [-1] * (N + 1)                  # 새로운 방문 리스트
bfs(max_node)

print(max(v_list))
