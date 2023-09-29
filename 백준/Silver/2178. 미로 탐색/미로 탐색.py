import sys
input = sys.stdin.readline
from collections import deque

# 상하좌우 탐색용 리스트
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

# 방문 리스트 초기화
v_list = [[0]*M for i in range(N)]
# 인접 리스트 초기화
A = [[0]*M for i in range(N)]

for i in range(N):
    num_list = list(input())
    for j in range(M):
        A[i][j] = int(num_list[j])

# BFS 구현
def bfs(i, j):
    queue = deque()
    v_list[i][j] = 1
    queue.append((i, j))
    while queue:
        cur = queue.popleft()
        if cur[0] == N - 1 and cur[1] == M - 1:
            print(v_list[cur[0]][cur[1]])
            return
        for k in range(4):
            x = cur[0] + dx[k]
            y = cur[1] + dy[k]
            if x >= 0 and y>=0 and x< N and y<M:
                if v_list[x][y] == 0 and A[cur[0]][cur[1]] != 0:

                    v_list[x][y] = v_list[cur[0]][cur[1]] + 1
                    queue.append((x, y))
bfs(0,0)