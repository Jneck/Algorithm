import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

N, M = map(int, input().split())

v_list = [False] * N
n_list = [[] for _ in range(N)]

is_possible = 0

def dfs(src, depth):
    v_list[src] = True
    global is_possible

    if depth == 4:
        is_possible = 1
        return

    new_depth = depth + 1
    for new_src in n_list[src]:
        if not v_list[new_src]:

            dfs(new_src, new_depth)

    # 다른 노드를 거쳐 올 경우 횟수가 커질 수 있음. 따라서 초기화를 통해 다른 노드 거쳐올 경우 대비
    v_list[src] = False

# 인접 리스트에 간선 설정
for i in range(M):
    node1, node2 = map(int, input().split())
    n_list[node1].append(node2)
    n_list[node2].append(node1)

for i in range(N):
    if is_possible == 1:
        break
    dfs(i, 0)

print(is_possible)