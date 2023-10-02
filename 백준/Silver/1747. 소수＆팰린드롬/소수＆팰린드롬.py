import sys

N = int(input())

A = [i for i in range(10**7+1)]
A[1] = 0

def is_p(num: str):
    if len(num) < 2:
        return True
    else:
        start = 0
        end = len(num)-1
        is_true = True
        while start < end:
            if num[start] != num[end]:
                is_true = False
                break
            start += 1
            end -= 1
        return is_true

for i in range(2, int((10**7)**(1/2)) + 1):
    if A[i] != 0:
        for j in range(i+i, len(A),i):
            A[j] = 0

for i in range(N, len(A)):
    if A[i] != 0 and is_p(str(A[i])):
        print(A[i])
        break
