import sys
sys.setrecursionlimit(10**6)
N = int(input())
M = int(input())

n_list = [i for i in range(N+1)]

def union_find(a):
    if a == n_list[a]:
        return a
    else:
        n_list[a] = union_find(n_list[a])
        return n_list[a]

def union(a, b):
    if a != n_list[a]:
        a = union_find(a)
    if b != n_list[b]:
        b = union_find(b)
    n_list[b] = a


for i in range(1, N+1):
    tmp_list = list(map(int, input().split()))
    for j in range(1, N+1):
        if tmp_list[j-1] == 1:
            union(i, j)

trip_list = list(map(int, input().split()))
represent_node = union_find(trip_list[0])
is_possible = True
for i in range(1, M):
    if represent_node != union_find(trip_list[i]):
        is_possible = False
        break

if is_possible:
    print("YES")
else:
    print("NO")