import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

n_list = [i for i in range(N+1)]

def union_find(a):
    if a == n_list[a]:
        return a
    else:
        n_list[a] = union_find(n_list[a])
        return n_list[a]

def union_know(a, b):
    a = union_find(n_list[a])
    b = union_find(n_list[b])
    # 진실을 아는 자가 있을 시 진실을 아는 것으로 설정
    if a == 0 :   # b가 진실을 모르는데 알게 됨 -> b의 집단들을 업데이트
        n_list[b] = 0
    elif b == 0:
        n_list[a] = 0
    else: # 진실을 모르는 사람들끼리 있으면 서로 합함
        n_list[b] = a

# 진실을 아는 자들은 모두 0으로 설정
know_list = list(map(int, input().split()))
for i in range(1, len(know_list)):
    n_list[know_list[i]] = 0

party = []
for i in range(M):
    participants = list(map(int, input().split()))
    party.append(participants)
    # 각 그룹에 union 작업을 진행 -> 아는 사람은 다 0으로 모르는 사람끼리는 합침
    for j in range(1, len(participants)-1):
        union_know(participants[j], participants[j+1])

# union find연산을 이용해서 대표값으로 모두 업데이트
for i in range(1, N+1):
    union_find(i)

answer = 0
for participants in party:
    can_tell_lie = True
    for j in range(1, len(participants)):
        if n_list[participants[j]] == 0:
            can_tell_lie = False
            break

    if can_tell_lie:
        answer += 1

print(answer)