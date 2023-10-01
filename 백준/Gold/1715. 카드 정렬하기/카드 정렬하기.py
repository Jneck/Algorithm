import sys

input = sys.stdin.readline
N = int(input())

from queue import PriorityQueue

pq = PriorityQueue()
answer = 0
for i in range(N):
    pq.put(int(input()))

while 1 != pq.qsize():
    new_card_bucket = pq.get() + pq.get()
    answer += new_card_bucket
    pq.put(new_card_bucket)

print(answer)
