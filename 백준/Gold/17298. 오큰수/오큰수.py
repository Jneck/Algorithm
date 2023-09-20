import sys
input = sys.stdin.readline

N = int(input())
num_arr = list(map(int, input().split()))
answer = ['-1']
tmp_s = []
for i in range(N-2, -1, -1):
    if num_arr[i+1] > num_arr[i]:
        tmp_s.append(num_arr[i+1])

    while tmp_s and tmp_s[-1] <= num_arr[i]:
        tmp_s.pop()
    if tmp_s:
        answer.append(str(tmp_s[-1]))
    else:
        answer.append(str(-1))
answer.reverse()
print(' '.join(answer))