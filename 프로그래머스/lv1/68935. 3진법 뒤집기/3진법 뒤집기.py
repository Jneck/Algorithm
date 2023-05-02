def solution(n):
    tmp3 = []
    while n != 0:
        tmp3.append(n%3)
        n = n // 3
    answer = 0
    for idx, num in enumerate(tmp3):
        answer += num*(3**(len(tmp3) - idx -1))
    return answer