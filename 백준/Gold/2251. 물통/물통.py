import sys
sys.setrecursionlimit(10**6)


A, B, C = map(int, input().split())
v_list = [[[False for i in range(C+1)] for i in range(B+1)] for i in range(A+1)]

def pour_water(a, b, c):
    global A, B, C
    v_list[a][b][c] = True
    if a != 0:
        if B >= (a+b):
            if not v_list[0][a+b][c]:
                pour_water(0, a+b, c)
        else:
            if not v_list[a+b-B][B][c]:
                pour_water(a+b-B, B, c)
        if C >= (a+c):
            if not v_list[0][b][a+c]:
                pour_water(0, b, a+c)
        else:
            if not v_list[a+c-C][b][C]:
                pour_water(a+c-C, b, C)
    if b != 0:
        if A >= (a+b):
            if not v_list[a+b][0][c]:
                pour_water(a+b, 0, c)
        else:
            if not v_list[A][a+b-A][c]:
                pour_water(A, a+b-A, c)
        if C >= (b+c):
            if not v_list[a][0][b+c]:
                pour_water(a, 0, b+c)
        else:
            if not v_list[a][b+c-C][C]:
                pour_water(a, b+c-C, C)
    if c != 0:
        if A >= (a+c):
            if not v_list[a+c][b][0]:
                pour_water(a+c, b, 0)
        else:
            if not v_list[A][b][a+c-A]:
                pour_water(A, b, a+c-A)
        if B >= (b+c):
            if not v_list[a][b+c][0]:
                pour_water(a, b+c, 0)
        else:
            if not v_list[a][B][b+c-B]:
                pour_water(a, B, b+c-B)

pour_water(0,0,C)

answer = [False for i in range(C+1)]

for j in range(B+1):
    for k in range(C+1):
        if v_list[0][j][k]:
            answer[k] = v_list[0][j][k]

for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')
