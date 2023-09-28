import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


N, M = map(int, input().split())
n_list = [[] for i in range(N+1)]

# 방문 리스트 생성하기
v_list = [False] * (N+1)

def dfs(src):
    # 방문한 지역 true
    v_list[src] = True

    # 다음 탐색 시작 호출
    for new_src in n_list[src]:
        # 방문하지 않았다면 dfs
        if not v_list[new_src]:
            dfs(new_src)

# 인접 리스트 초기화하기
for i in range(M):
    node1, node2 = map(int, input().split())
    n_list[node1].append(node2)
    n_list[node2].append(node1)


# dfs 실행 및 분리 그래프 세기
answer = 0
for i in range(1, N+1):
    if not v_list[i]:
        answer += 1
        dfs(i)
print(answer)