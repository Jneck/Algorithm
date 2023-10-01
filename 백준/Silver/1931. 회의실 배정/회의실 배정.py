import sys

input = sys.stdin.readline

N = int(input())

from queue import PriorityQueue

pq = PriorityQueue()

for i in range(N):
    start, end = map(int, input().split())
    pq.put((end, start))

answer = 0
finish_time = 0
while not pq.empty():
    end, start = pq.get()
    if finish_time <= start:
        finish_time = end
        answer += 1

print(answer)
