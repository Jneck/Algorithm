import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())

n_list = []
v_list = []
is_possible = True
def dfs(cur_node, group_num):
    global is_possible
    for new_node in n_list[cur_node]:
        if not is_possible:
            break
        if v_list[new_node] == 0:
            if group_num == 1:
                v_list[new_node] = 2
            else:
                v_list[new_node] = 1
            dfs(new_node, v_list[new_node])
        elif v_list[new_node] == 1:
            if group_num == 1:
                is_possible = False
                break
        else:
            if group_num == 2:
                is_possible = False
                break



for t_cnt in range(T):
    V, E = map(int, input().split())
    n_list = [[] for i in range(V + 1)]
    v_list = [0] * (V + 1)
    is_possible = True
    for i in range(E):
        node1, node2 = map(int, input().split())
        n_list[node1].append(node2)
        n_list[node2].append(node1)

    for i in range(1, V+1):
        if v_list[i] == 0:
            dfs(i, 1)
            if not is_possible:
                is_possible = True
                dfs(i, 2)
                if not is_possible:
                    break

    if is_possible:
        print('YES')
    else:
        print('NO')


