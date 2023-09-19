import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
A_list = list(map(int, input().split()))
tmp_deque = deque()
for i in range(N):
    current_num = A_list[i]
    # 맨 뒤에서부터 자기보다 작은 값 제거
    while tmp_deque and tmp_deque[-1][1] >= current_num:
        tmp_deque.pop()
    tmp_deque.append((i, current_num))
    # 맨앞 인덱스 같으면 제거하기
    if tmp_deque[0][0] == i-L:
        tmp_deque.popleft()
    print(tmp_deque[0][1], end=' ')


