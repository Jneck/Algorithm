import sys
input = sys.stdin.readline

from queue import PriorityQueue
pq = PriorityQueue()


N = int(input())
for _ in range(N):
    pq.put(int(input()))

answer = 0
while True:
    min_size = pq.get()
    if pq.empty():
        break
    second_min_size = pq.get()

    new_size = min_size + second_min_size
    answer += new_size
    
    pq.put(new_size)

print(answer)