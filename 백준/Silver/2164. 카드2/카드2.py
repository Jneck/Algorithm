import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
card_queue = deque([i for i in range(1, N+1)])

for i in range(N-1):
    card_queue.popleft()
    card_queue.append(card_queue.popleft())
print(card_queue.pop())