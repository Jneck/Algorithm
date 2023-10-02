import math


A, B = map(int, input().split())

arr = [i for i in range(int(math.sqrt(B)) + 1)]
arr[1] = 0

for i in range(2, len(arr)):
    if arr[i] != 0:
        for j in range(i+i, len(arr),i):
            arr[j] = 0

cnt = 0

for i in range(2, int(math.sqrt(B)) + 1):
    # 소수일 경우
    if arr[i] != 0:
        tmp_idx = 2
        tmp_num = arr[i] ** tmp_idx
        while tmp_num <= B:
            if A <= tmp_num:
                cnt += 1
            tmp_idx += 1
            tmp_num = arr[i] ** tmp_idx

print(cnt)