import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def union_find(a):
    if union_list[a] == a:
        return a
    else:
        union_list[a] = union_find(union_list[a])
        return union_list[a]


def union(a, b):
    union_list[a] = union_find(b)
    union_list[b] = union_list[a]


V, E = list(map(int, input().split()))
edge_list = []
union_list = [i for i in range(V + 1)]

for i in range(E):
    edge_data = list(map(int, input().split()))
    edge_list.append(edge_data)

edge_list.sort(key=lambda x: x[2])
cnt = 0
edge_len = 0

if V != 1:
    for edge_data in edge_list:
        a = union_find(edge_data[0])
        b = union_find(edge_data[1])
        if a != b:
            union_list[a] = b
            edge_len += edge_data[2]
            cnt += 1
            if cnt == V - 1:
                break
print(edge_len)
