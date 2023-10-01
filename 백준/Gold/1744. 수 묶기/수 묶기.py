import sys
input = sys.stdin.readline

N = int(input())

A1 = []
A2 = []
for i in range(N):
    num = int(input())
    if num <= 0:
        A1.append(num)
    else:
        A2.append(num)
A1.sort()
A2.sort(reverse=True)

answer_list = []

# A1에 대해서 작업
idx = 0
while idx < len(A1):
    num = A1[idx]
    idx += 1
    if idx == len(A1):
        answer_list.append(num)
        break
    else:
        next_num = A1[idx]
        answer_list.append(num * next_num)
        idx += 1



idx = 0
while idx < len(A2):
    num = A2[idx]
    idx += 1
    # 숫자가 1일 경우 안 곱하는 게 이득
    if num == 1:
        answer_list.append(num)
        continue
    if idx == len(A2):
        answer_list.append(num)
        break
    else:
        next_num = A2[idx]
        idx += 1
        # 숫자가 1일 경우 안 곱하는 게 이득
        if next_num == 1:
            answer_list.append(num)
            answer_list.append(next_num)
        else:
            answer_list.append(num * next_num)

print(sum(answer_list))
