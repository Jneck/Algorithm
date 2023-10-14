import sys
input = sys.stdin.readline
print = sys.stdout.write

from queue import PriorityQueue

N, M, K = map(int, input().split())

n_list = [[] for i in range(N+1)]
sp_list = [[3*(10**9) for j in range(K)] for i in range(N+1)]

for i in range(M):
    u, v, w = map(int, input().split())
    n_list[u].append([v, w])

my_pq = PriorityQueue()

sp_list[1][0] = 0
my_pq.put([0, 1])

while not my_pq.empty():
    cur_node_set = my_pq.get()
    sp = cur_node_set[0]
    cur_node = cur_node_set[1]
    for new_node_set in n_list[cur_node]:
        new_node = new_node_set[0]
        weight = new_node_set[1]
        if sp_list[new_node][-1] > weight + sp:
            sp_list[new_node][-1] = weight+sp
            sp_list[new_node].sort()
            my_pq.put([weight+sp, new_node])

for i in range(1, N+1):
    if sp_list[i][K-1] == 3*(10**9):
        print('-1\n')
    else:
        print(str(sp_list[i][K-1]) + '\n')