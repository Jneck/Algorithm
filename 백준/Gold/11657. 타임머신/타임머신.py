import sys
input = sys.stdin.readline
print = sys.stdout.write

INF = 10**8
N, M = map(int, input().split())
sp_list = [INF for i in range(N+1)]
e_list = [[] for i in range(M+1)]

# 에지 리스트 초기화
for i in range(1, M+1):
    e_list[i] = list(map(int, input().split()))

# sp_list 초기값 설정
sp_list[1] = 0

def bellman_ford():
    for j in range(1, N):
        for i in range(1, M+1):
            # 출발 노드가 방문한 적이 없는 노드일 때 값을 업데이트하지 않음
            s, d, w = e_list[i]
            if sp_list[s] != INF:
                if sp_list[d] > sp_list[s] + w:
                    sp_list[d] = sp_list[s] + w
    for i in range(1, M + 1):
        # 출발 노드가 방문한 적이 없는 노드일 때 값을 업데이트하지 않음
        s, d, w = e_list[i]
        if sp_list[s] != INF:
            if sp_list[d] > sp_list[s] + w:
                break
    else: # 끝까지 다 마쳐서 음수 사이클 존재하지 않으면
        return True
    return False

is_possible = bellman_ford()
if is_possible:
    for i in range(2, N+1):
        if sp_list[i] == INF:
            print('-1\n')
        else:
            print(str(sp_list[i]) + '\n')

else:
    print('-1')