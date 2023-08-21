import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph_list = []

for i in range(N):
    graph_list.append(list(map(int, input().split())))

sum_graph_list = []

for i in range(N):
    dummy_list = []
    for j in range(N):
        dummy_list.append(0)
    sum_graph_list.append(dummy_list)
for i in range(N):
    for j in range(N):
        if (i == 0) and (j == 0) :
            sum_graph_list[0][0] = graph_list[0][0]
        elif i == 0:
            sum_graph_list[i][j] = graph_list[i][j] + sum_graph_list[i][j-1]
        elif j == 0:
            sum_graph_list[i][j] = graph_list[i][j] + sum_graph_list[i-1][j]
        else:
            sum_graph_list[i][j] = graph_list[i][j] + sum_graph_list[i][j-1] + sum_graph_list[i-1][j] - sum_graph_list[i-1][j-1]
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 == 1) and (y1 == 1):
        print(sum_graph_list[x2-1][y2-1])
    elif x1 == 1:
        print(sum_graph_list[x2-1][y2-1] - sum_graph_list[x2-1][y1-2])
    elif y1 == 1:
        print(sum_graph_list[x2-1][y2-1] - sum_graph_list[x1-2][y2-1])
    else:
        print(sum_graph_list[x2-1][y2-1] - sum_graph_list[x1-2][y2-1] - sum_graph_list[x2-1][y1-2] + sum_graph_list[x1-2][y1-2])