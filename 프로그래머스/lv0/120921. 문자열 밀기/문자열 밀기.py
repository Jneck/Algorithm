def solution(A, B):
    answer = -1
    for i in range(len(A)):
        if B == (A[-i:] + A[:-i]):
            answer = i
            break
    return answer