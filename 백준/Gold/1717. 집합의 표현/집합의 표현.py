import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

n_list = [i for i in range(n+1)]

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

for i in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a, b)
    else:
        if union_find(a) == union_find(b):
            print('YES\n')
        else:
            print('NO\n')