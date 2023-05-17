def solution(t, p):
    answer = 0
    len_p = len(p)
    for i in range(len(t) - len_p + 1):
        if int(t[i:i+len_p]) <= int(p):
            answer += 1
    return answer