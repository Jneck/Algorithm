import sys
input = sys.stdin.readline
print = sys.stdout.write

from queue import PriorityQueue
pq = PriorityQueue()

n, m, k = list(map(int, input().split()))
node_list = [[] for i in range(n+1)]
node_path_list = [[sys.maxsize for j in range(k)] for i in range(n+1)]

for i in range(m):
    a, b, c = list(map(int, input().split()))
    node_list[a].append([b, c])

node_path_list[1][0] = 0
pq.put([0, 1])
while not pq.empty():
    pq_data = pq.get()
    path_len = pq_data[0]
    node = pq_data[1]

    for next_node_data in node_list[node]:
        next_node = next_node_data[0]
        new_len = path_len + next_node_data[1]

        if new_len < node_path_list[next_node][-1]:
            node_path_list[next_node][-1] = new_len
            node_path_list[next_node].sort()
            pq.put([new_len, next_node])

for node_path in node_path_list[1:]:
    if node_path[-1] != sys.maxsize:
        print(f'{node_path[-1]}\n')
    else:
        print('-1\n')