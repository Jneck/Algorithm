import sys
input = sys.stdin.readline
print = sys.stdout.write

M, N = map(int, input().split())

A = [i for i in range(N+1)]
A[1] = 0

for i in range(2, int(N**(1/2)) + 1):
    if A[i] != 0:
        for j in range(i+i, N+1, i):
            A[j] = 0

for i in range(M, N+1):
    if A[i] != 0:
        print(str(A[i]) + "\n")