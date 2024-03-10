import sys
input = sys.stdin.readline
print = sys.stdout.write

from queue import PriorityQueue

my_pq = PriorityQueue()
V, E = map(int, input().split())

n_list = [[] for i in range(V+1)]
sp_list = [5*(10**7) for i in range(V+1)]
v_list = [False for i in range(V+1)]

s_node = int(input())
for i in range(E):
    u, v, w = map(int, input().split())
    n_list[u].append([v, w])
    
# 인접 리스트 만들기 종료

sp_list[s_node] = 0
my_pq.put((0, s_node))
while not my_pq.empty():
    cur_node = my_pq.get()[1]
    if not v_list[cur_node]:
        v_list[cur_node] = True
        for new_node_set in n_list[cur_node]:
            new_node = new_node_set[0]
            if not v_list[new_node] and sp_list[new_node] > sp_list[cur_node] + new_node_set[1]:
                sp_list[new_node] = sp_list[cur_node] + new_node_set[1]
                my_pq.put([sp_list[new_node], new_node])

for i in range(1, V+1):
    if sp_list[i] != 5*(10**7):
        print(str(sp_list[i]) + "\n")
    else:
        print('INF\n')