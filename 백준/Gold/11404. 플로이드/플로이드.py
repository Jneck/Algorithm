import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())

sp_list = [[sys.maxsize for j in range(n + 1)] for i in range(n + 1)]

for i in range(len(sp_list)):
    sp_list[i][i] = 0

for i in range(m):
    a, b, c = list(map(int, input().split()))
    sp_list[a][b] = min(sp_list[a][b], c)


def floyd_warshall():
    for k in range(1, n + 1):  # k가 가장 바깥쪽이어야 함
        for s in range(1, n + 1):
            for e in range(1, n + 1):
                sp_list[s][e] = min(sp_list[s][e], sp_list[s][k] + sp_list[k][e])

floyd_warshall()
for i in range(1, n+1):
    for j in range(1, n + 1):
        if sp_list[i][j] == sys.maxsize:
            print('0 ')
        else:
            print(f'{sp_list[i][j]} ')
    print('\n')