def solution(n):
    answer = 0
    for i in range(1, n+1):
        while True:
            answer += 1
            if ('3' not in str(answer)) and ((answer)%3 != 0):
                break
    return answer