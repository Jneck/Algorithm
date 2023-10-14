import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

INF = -2*(10**8)
N, s_node, f_node, M = map(int, input().split())
e_list = [[]for i in range(M)]
mp_list = [INF for i in range(N)]
n_list = [[] for i in range(N)]
for i in range(M):
    e_list[i] = list(map(int, input().split()))
    # 역방향 인접 리스트
    n_list[e_list[i][0]].append(e_list[i][1])

# 간선의 정확한 가중치 저장
nw_list = list(map(int, input().split()))
for i in range(M):
    e_list[i][2] = nw_list[e_list[i][1]] - e_list[i][2]


# f_node와 연결되어 있는지 확인을 위한 dfs
v_list = [False for i in range(N)]
def dfs(cur_node, target_node):
    if cur_node == target_node:
        return
    for new_node in n_list[cur_node]:
        if not v_list[new_node]:
            v_list[new_node] = True
            dfs(new_node, target_node)

def check_f_node(node, target_node):
    for i in range(N):
        v_list[i] = False
    v_list[node] = True
    dfs(node, target_node)
    if v_list[target_node]:
        return True
    else:
        return False

def bellman_ford():
    for i in range(N-1):
        for j in range(M):
            s, d, w = e_list[j]
            if mp_list[d] < mp_list[s] + w:
                mp_list[d] = mp_list[s] + w
    for j in range(M):
        s, d, w = e_list[j]
        # 양수 사이클이 존재하고 f_node로 도달할 수 있을 때
        if mp_list[d] < mp_list[s] + w:
            if (check_f_node(d, f_node) and check_f_node(s_node, d)) or (check_f_node(s, f_node) and check_f_node(s_node, s)):
                break
    else:
        return True
    return False

mp_list[s_node] = nw_list[s_node]
if N != 1:
    is_possible = bellman_ford()
    if check_f_node(s_node, f_node):
        if is_possible:
            print(mp_list[f_node])
        else:
            print('Gee')
    else:
        print('gg')
else: # 노드가 1개일 때는 벨만 포드가 아예 돌지 않음
    is_gee = False
    for j in range(M):
        s, d, w = e_list[j]
        if mp_list[d] < mp_list[s] + w:
            is_gee = True
            break
    if is_gee:
        print('Gee')
    else:
        print(mp_list[f_node])