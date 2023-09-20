import sys
input = sys.stdin.readline
print = sys.stdout.write

from queue import PriorityQueue
myQueue = PriorityQueue()

N = int(input())


for i in range(N):
    x = int(input())
    if x == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1])) + '\n')
    else:
        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        # 파이썬에서 priority queue는 데이터의 순서가 정렬 우선순위가 된다. (절댓값, 실제값) 튜플로 삽입.
        myQueue.put((abs(x), x))