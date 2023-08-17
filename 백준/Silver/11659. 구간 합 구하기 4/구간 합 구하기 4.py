import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int,input().split()))
sum_list = [num_list[0]]
for i in range(1, len(num_list)):
  sum_list.append(sum_list[-1] + num_list[i])
for i in range(M):
  start, end = map(int,input().split())
  if start == 1:
    print(sum_list[end-1])
  else:
    print(sum_list[end-1] - sum_list[start-2])